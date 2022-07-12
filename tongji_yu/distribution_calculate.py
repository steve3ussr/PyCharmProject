import math


class DistributionCalculate(object):
    def __init__(self, diameter_total, thick_outer, thick_inner, counts_hole):
        self.r_total = diameter_total / 2 - thick_outer  # 最大可用半径
        self.area_total = self.r_total ** 2 * math.pi  # 最大可用面积
        self.counts_hole = counts_hole  # 孔的数量
        self.area_per_tube = self.area_total / self.counts_hole  # 平均面积
        self.r_avg = math.sqrt(self.area_per_tube / math.pi)  # 平均面积对应的半径
        self.counts_hole_rest = None  # 需要分配位置的孔的数量
        self.r_available = None  # 需要分配位置的孔的可用环形半径
        self.central_hole_existence = None  # 是否存在中心孔
        self.r_central = None  # 中心半径, 0 or self.r_avg

        if self.judge_prime():
            self.counts_hole_rest = self.counts_hole - 1
            self.r_available = self.r_total - self.r_avg
            self.central_hole_existence = True
            self.r_central = self.r_avg
        else:
            self.counts_hole_rest = self.counts_hole
            self.r_available = self.r_total
            self.central_hole_existence = False
            self.r_central = 0

    def judge_prime(self) -> bool:
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

    def calc_sector_radial_list(self): pass
    """
    计算一个扇区内各环形的径向尺寸列表
    """

    def judge_ring_hole_counts(self): pass
    """
    判断一环的孔的数量是否合适：第一层能否放得下
    """


if __name__ == "__main__":
    pass
