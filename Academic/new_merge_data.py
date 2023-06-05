import os
import pandas as pd
import re
from pprint import pprint


class MergeData:
    def __init__(self, dir_root, boundary, ts_init, ts_end, list_coord=None, list_phy_var=None):
        self.__dir_root = dir_root
        self.__boundary = boundary
        self.__ts_init = ts_init
        self.__ts_end = ts_end

        self.__list_coord = ['X_(m)', 'Y_(m)', 'Z_(m)'] if list_coord is None else list_coord
        self.__list_phy_var = ['Pressure_(Pa)', 'Acoustic_Pressure_(Pa)'] if list_phy_var is None else list_phy_var

        self.__coord = None
        self.res = {_: None for _ in list_phy_var}

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

    def __load_csv_cal_coord(self, prefix, id):

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
            self.coord = data_ori.loc[:, self.__list_coord]
        except AssertionError:
            raise AssertionError(f"ERROR: coord unequal from: {prefix}::{id}")

        # concat
        for phy_var in self.__list_phy_var:
            # TODO: change Timestep_id to second
            _ = data_ori.loc[:, phy_var].to_frame(name=f"{(id-1000)*5e-05+0.5}")
            if self.res[phy_var] is None:
                self.res[phy_var] = _
            else:
                if len(_.index) != len(self.res[phy_var].index):
                    raise IndexError
                self.res[phy_var] = pd.concat([self.res[phy_var], _], axis=1)

    def exec(self, time_begin, time_step):
        for i in range(self.__ts_init, self.__ts_end + 1):
            self.__load_csv_cal_coord(f"{self.__dir_root}\\{self.__boundary}_table_", i)

        for phy_var in self.__list_phy_var:
            _ = self.res[phy_var].mean(axis=0)
            _.index = [time_begin + time_step * i for i in range(len(_))]
            _.to_csv(f"{self.__dir_root}\\AVG_{phy_var}_{self.__boundary}.csv")

            self.res[phy_var] = pd.concat([self.coord, self.res[phy_var]], axis=1)
            self.res[phy_var].to_csv(f"{self.__dir_root}\\TS_{phy_var}_{self.__boundary}.csv", index=False)

        print(f"COMPLETED: {self.__boundary}")


if __name__ == '__main__':
    path = r"T:\stage3\GAC_cavEnabled_reCalc_smallstepAPE_0.6s_morePhyVar_11probes\Tensor_GradP_Vol_AP_P"
    lst_boundary = [i for i in os.listdir(path) if os.path.isdir(f"{path}\\{i}")]
    # lst_boundary.remove('smallstep_Z1.3_pressure')
    # lst_boundary = lst_boundary[22:]
    lst_boundary = lst_boundary[0:20]

    pprint(lst_boundary)

    for i in lst_boundary:
        pass

        MergeData(f"{path}\\{i}", i, 3001, 6000).exec(0.6, 1/20000)

