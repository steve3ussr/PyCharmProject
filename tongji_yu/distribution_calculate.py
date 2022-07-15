import math


class DistributionCalculate(object):
    def __init__(self, *, diameter_total, thick_outer, diameter_hole, thick_inner, counts_hole):
        self.r_total = diameter_total / 2 - thick_outer  # 最大可用半径
        self.r_tube = thick_inner + diameter_hole / 2  # 管子外半径
        self.d_tube = self.r_tube * 2  # 管子外直径
        self.area_total = self.r_total ** 2 * math.pi  # 最大可用面积
        self.counts_hole = counts_hole  # 孔的数量
        self.area_per_tube = self.area_total / self.counts_hole  # 平均面积
        self.r_avg = math.sqrt(self.area_per_tube / math.pi)  # 平均面积对应的半径

        self.counts_hole_rest = None  # 需要分配位置的孔的数量
        self.r_available = None  # 需要分配位置的孔的可用环形半径
        self.central_hole_existence = None  # 是否存在中心孔
        self.r_central = None  # 中心半径, 0 or self.r_avg

        self.radial_distribution = None  # 径向尺寸列表(每一层的径向尺寸)

        if self.__judge_prime():
            self.counts_hole_rest = self.counts_hole - 1
            self.r_available = self.r_total - self.r_avg
            self.central_hole_existence = True
            self.r_central = self.r_avg
        else:
            self.counts_hole_rest = self.counts_hole
            self.r_available = self.r_total
            self.central_hole_existence = False
            self.r_central = 0

    def __judge_prime(self) -> bool:
        """
        判断 self.counts_hole 即 孔数是否为质数
        """
        if self.counts_hole == 1:
            return False
        elif self.counts_hole == 2:
            return True
        else:
            pass

        max_potential = math.ceil(math.sqrt(self.counts_hole))
        for i in range(2, max_potential + 1):
            res = self.counts_hole % i
            if res == 0:
                return False
            else:
                continue
        return True

    def __calc_sector_radial_list(self, counts_ring: int):
        """
        指定环的数量, 按照等面积计算各环形的径向尺寸列表
        还需要:
        self.r_available
        self.r_central
        self.r_total
        3个中有2个就行
        """
        avg_area = (self.r_total ** 2 - self.r_central ** 2) / counts_ring
        r_current = self.r_central
        res_list = []
        for i in range(counts_ring):
            tmp = math.sqrt(avg_area + r_current ** 2) - r_current
            if tmp < self.d_tube:
                return False
            else:
                res_list.append(tmp)
                r_current += tmp
        self.radial_distribution = res_list
        return True

    def __judge_ring_hole_counts(self, counts_1layer_holes: int) -> bool:
        """
        判断一环的孔的数量是否合适：第一层能否放得下
        """
        assert self.radial_distribution is not None, 'radial distribution non-exists'
        r = self.radial_distribution[0] + self.r_central - self.r_tube
        angle_per_tube = math.asin((r - self.r_tube) / r) * 2
        return False if angle_per_tube * counts_1layer_holes > 360 else True

    def temp(self):
        pass

    def exec(self):
        res = []
        for i in range(2, self.counts_hole_rest):
            if self.counts_hole_rest / i == (a_ring_hole_counts := self.counts_hole_rest // i):
                pass
            else:
                continue

            if self.__calc_sector_radial_list(i):
                if self.__judge_ring_hole_counts(a_ring_hole_counts):

                    temp_list = [self.r_central] * i
                    for index, value in self.radial_distribution:
                        temp_list[index] = self.r_central + i/2




                    res.append(f'共分配 {self.counts_hole_rest} 个孔, 分成{i} 环, 每环 {a_ring_hole_counts} 个, 中心半径: {self.r_central}, 各环径向尺寸: {}')
                else:
                    continue
            else:
                continue

        if res:
            cnt = 0
            for x in res:
                cnt += 1
                print(f'方案 {cnt}: ' + x)
        else:
            raise TimeoutError('分配失败')


if __name__ == "__main__":
    DistributionCalculate(diameter_total=99, thick_outer=1.5, diameter_hole=1.5, thick_inner=1.5, counts_hole=70).exec()
