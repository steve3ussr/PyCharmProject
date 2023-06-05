import functools
import os
import pandas as pd
import re
from pprint import pprint
import time
import polars
from multiprocessing import Pool


def timer(func, *args, **kwargs):
    @functools.wraps(func)
    def _timer():
        t_start = time.time()
        _ = func(*args, **kwargs)
        t_end = time.time()
        print(f"FUNCTION: {str(func)}, exec time: {t_end - t_start}")
        return _
    return _timer


class MergeData:
    def __init__(self, dir_root, boundary, ts_init, ts_end, list_coord=None, list_phy_var=None):
        self.__dir_root = dir_root
        self.__boundary = boundary
        self.__ts_init = ts_init
        self.__ts_end = ts_end

        self.__list_coord = ['X_(m)', 'Y_(m)', 'Z_(m)'] if list_coord is None else list_coord
        self.__list_phy_var = ['Pressure_(Pa)', 'Acoustic_Pressure_(Pa)'] if list_phy_var is None else list_phy_var

        self.__coord = None
        self.res = {_: None for _ in self.__list_phy_var}

    @staticmethod
    def __check_valid_file(s):
        assert os.path.isfile(s), f"ERROR: csv file pre-check failed, {s} isn't valid path."

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, df):
        if self.__coord is None:
            self.__coord = df
        else:
            assert self.__coord[:].equals(df)

    def _load_csv_cal_coord(self, id):
        prefix = f"{self.__dir_root}\\{self.__boundary}_table_"

        abspath = f"{prefix}{id}.csv"
        self.__check_valid_file(abspath)
        print(f"LOADING: {prefix}::{id}")
        data_ori = pd.read_csv(abspath).rename(columns=lambda x: re.sub(' ', '_', x))
        data_ori = data_ori.sort_values(by=self.__list_coord,
                                        ascending=[True, True, True],
                                        kind='quicksort',
                                        ignore_index=True)

        # check coord
        try:
            if self.__coord is None:
                self.__coord = data_ori.loc[:, self.__list_coord]
            else:
                assert self.__coord.equals(data_ori.loc[:, self.__list_coord])
        except AssertionError:
            raise AssertionError(f"ERROR: coord unequal from: {prefix}::{id}")

        # concat
        for phy_var in self.__list_phy_var:
            # TODO: change Timestep_id to second
            _ = data_ori.loc[:, phy_var].to_frame(name=f"{(id-1000)*5e-05+0.5}")

            self.res[phy_var] = pd.concat([self.res[phy_var], _], axis=1)
            continue

            if self.res[phy_var] is None:
                self.res[phy_var] = _
            else:
                if len(_.index) != len(self.res[phy_var].index):
                    raise IndexError
                self.res[phy_var] = pd.concat([self.res[phy_var], _], axis=1)

    def _load_csv_cal_coord_v2(self, id):
        prefix = f"{self.__dir_root}\\{self.__boundary}_table_"

        abspath = f"{prefix}{id}.csv"
        self.__check_valid_file(abspath)
        print(f"LOADING: {prefix}::{id}")
        data_ori = pd.read_csv(abspath).rename(columns=lambda x: re.sub(' ', '_', x))
        data_ori = data_ori.sort_values(by=self.__list_coord,
                                        ascending=[True, True, True],
                                        kind='quicksort',
                                        ignore_index=True)

        # check coord

        try:
            if self.__coord is None:
                self.__coord = data_ori.loc[:, self.__list_coord]
            else:
                assert self.__coord.equals(data_ori.loc[:, self.__list_coord])
        except AssertionError:
            raise AssertionError(f"ERROR: coord unequal from: {prefix}::{id}")


        # concat
        return [data_ori.loc[:, phy_var].to_frame(name=f"{(id-1000)*5e-05+0.5}") for phy_var in self.__list_phy_var]

    def exec(self, time_begin, time_step):
        """
        for i in range(self.__ts_init, self.__ts_end + 1):
            self._load_csv_cal_coord(i)

        """
        with Pool(processes=16) as pool:
            csv_data = pool.map(self._load_csv_cal_coord_v2, range(self.__ts_init, self.__ts_end + 1))

        for i, phy_var in enumerate(self.__list_phy_var):
            tmp = [_[i] for _ in csv_data]
            self.res[phy_var] = pd.concat(tmp, axis=1)



        for phy_var in self.__list_phy_var:
            _ = self.res[phy_var].mean(axis=0)
            _.index = [time_begin + time_step * i for i in range(len(_))]
            _.to_csv(f"{self.__dir_root}\\AVG_{phy_var}_{self.__boundary}.csv")

            # self.res[phy_var] = pd.concat([self.coord, self.res[phy_var]], axis=1)
            # print(self.res[phy_var])
            # self.res[phy_var].to_csv(f"{self.__dir_root}\\TS_{phy_var}_{self.__boundary}.csv", index=False)
            # self.res[phy_var].to_hdf(f"{self.__dir_root}\\TS_{phy_var}_{self.__boundary}.h5", 'table', index=False)
            # _ = polars.from_pandas(self.res[phy_var])
            # _.write_csv(f"{self.__dir_root}\\TS_{phy_var}_{self.__boundary}_MULTI_POLARS.csv", batch_size=2048)

        print(f"COMPLETED: {self.__boundary}")


if __name__ == '__main__':

    # log
    # 5700X USB3.0 m.2
    # pandas.DataFrame.to_csv                      exec time: 275.78269505500793
    # pandas.DataFrame.to_hdf                      exec time: 182.8802468776703
    # polars.DataFrame.write_csv, batch_size=2048, exec time: 185.7497913837433

    # not-export, read only,    ORIGINAL           exec time: 167.24301767349243
    # not-export, read only, ASSERT coord,         exec time: 170.0869140625

    # Pool(16).map, read only,                     exec time: 23.352866172790527
    # Pool(16).map, polars.write_csv,              exec time: 29.757362604141235

    @timer
    def main():
        path = r"S:\benchmark"
        lst_boundary = [i for i in os.listdir(path) if os.path.isdir(f"{path}\\{i}")]

        pprint(lst_boundary)

        for i in lst_boundary:
            MergeData(f"{path}\\{i}", i, 3001, 3300, list_phy_var=['Acoustic_Pressure_(Pa)']).exec(0.6, 1/20000)

    main()




