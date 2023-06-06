import functools
import os
import re
from pprint import pprint
from multiprocessing import Pool

import pandas as pd
import polars


class MergeData:
    def __init__(self,
                 dir_root, boundary,
                 ts_init, ts_end, appendix,
                 time_phy_start, time_phy_step,
                 list_coord=None,
                 list_phy_var=None):

        if list_coord is None:
            list_coord = ['X_(m)', 'Y_(m)', 'Z_(m)']
        if list_phy_var is None:
            list_phy_var = ['Pressure_(Pa)', 'Acoustic_Pressure_(Pa)']

        self._dir_root = dir_root  # 存放很多个boundary文件夹的文件夹
        self._boundary = boundary  # 这些boundary的名字
        self._ts_init = ts_init  # (ts: timestep)第一个时间步        3001
        self._ts_end = ts_end  # (ts: timestep)最后的时间步        6000
        self._appendix = appendix  # STAR-CCM+表格后缀(默认为table)
        self._time_phy_start = time_phy_start  # 第一个物理时间                    0.6+5e-5
        self._time_phy_step = time_phy_step  # 物理时间步长                      5e-5
        self._list_coord = list_coord  # 坐标(默认值如上所述)
        self._list_phy_var = list_phy_var  # 待处理的物理量名字(默认值如上所述)

        self._csv_prefix = f"{self._dir_root}\\{self._boundary}_{self._appendix}_"

        self.__coord = None  # 内部用来验证坐标一致性的变量
        self.res = {_: None for _ in self._list_phy_var}  # 数据处理结果

    def _load_csv_check_coord(self, timestep_id, mode=0):
        # pre-check file path valid
        abspath = f"{self._csv_prefix}{timestep_id}.csv"
        assert os.path.isfile(abspath), f"ERROR: csv file pre-check failed, {abspath} isn't valid path."
        print(f"LOADING: {self._csv_prefix}::{timestep_id}")

        # pandas.read_csv
        data_ori = pd.read_csv(abspath).rename(columns=lambda x: re.sub(' |:', '_', x))
        data_ori = data_ori.sort_values(by=self._list_coord,
                                        ascending=[True, True, True],
                                        kind='quicksort',
                                        ignore_index=True)

        if mode == 0:
            try:
                assert self.__coord.equals(data_ori.loc[:, self._list_coord])
            except AssertionError:
                raise AssertionError(f"ERROR: coord unequal from: {self._csv_prefix}::{id}")

            time_phy_curr = (timestep_id - self._ts_init) * self._time_phy_step + self._time_phy_start
            return [data_ori.loc[:, phy_var].to_frame(name=f"{time_phy_curr}") for phy_var in self._list_phy_var]

        elif mode == 1:
            self.__coord = data_ori.loc[:, self._list_coord]

            time_phy_curr = (timestep_id - self._ts_init) * self._time_phy_step + self._time_phy_start
            for phy_var in self._list_phy_var:
                self.res[phy_var] = data_ori.loc[:, phy_var].to_frame(name=f"{time_phy_curr}")
            return

    def _export_phy_var(self, k):
        _ = polars.from_pandas(self.res[k])
        _.write_csv(f"{self._dir_root}\\TS_{k}_{self._boundary}_MULTI_POLARS_v2.csv", batch_size=2048)
        print(f"COMPLETED: {self._boundary}::{k}")

    def exec(self, np=8):
        self._load_csv_check_coord(self._ts_init, mode=1)

        with Pool(processes=np) as pool_read:
            csv_data = pool_read.map(self._load_csv_check_coord, range(self._ts_init + 1, self._ts_end + 1))

        for i, phy_var in enumerate(self._list_phy_var):
            # extract data, export AVG_
            tmp_df = pd.concat([_[i] for _ in csv_data], axis=1)
            self.res[phy_var] = pd.concat([self.res[phy_var], tmp_df], axis=1)

            _ = self.res[phy_var].mean(axis=0)
            _.index = [self._time_phy_start + self._time_phy_step * i for i in range(len(_))]
            _.to_csv(f"{self._dir_root}\\AVG_{phy_var}_{self._boundary}_v2.csv")

            self.res[phy_var] = pd.concat([self.__coord, self.res[phy_var]], axis=1)

        with Pool(processes=2) as pool_write:
            pool_write.map(self._export_phy_var, self._list_phy_var)


if __name__ == '__main__':
    import time


    def timer(func, *args, **kwargs):
        @functools.wraps(func)
        def _timer():
            t_start = time.time()
            _ = func(*args, **kwargs)
            t_end = time.time()
            print(f"FUNCTION: {str(func)}, exec time: {t_end - t_start}")
            return _

        return _timer


    @timer
    def main():
        path = r"S:\stage2"
        lst_boundary = [i for i in os.listdir(path) if os.path.isdir(f"{path}\\{i}")]

        pprint(lst_boundary)

        for i in lst_boundary:
            MergeData(dir_root=f"{path}\\{i}",
                      boundary=i,
                      ts_init=3001,
                      ts_end=6000,
                      appendix='table',
                      time_phy_start=0.6 + 5E-5,
                      time_phy_step=5E-5,
                      list_coord=None,
                      list_phy_var=['Acoustic_Pressure_(Pa)']).exec(16)


    main()

    # benchmark
    # 5700X  USB3.0
    #
    # read only, np=1                exec time: 149.58892607688904
    # read only, np=8                exec time: 30.50161838531494
    # read only, np=16               exec time: 23.55579423904419
    # read + process, np=16          exec time: 24.56181526184082
    # read + process + export        exec time: 30.386018991470337
    #
    # AMD EPYC 7742 (64 Core, 128 Processor)
    # read only, np=1                exec time: 179.00459146499634
    # read only, np=8                exec time: 28.68432092666626
    # read only, np=16               exec time: 17.245872259140015
    # read only, np=61               exec time: 7.604947566986084
    # read + process, np=61          exec time: 9.413570880889893
    # read + process + export, np=61 exec time: 864.4292280673981
