import math


class DistributionCalculate(object):
    def __init__(self, n):
        self.r_total = 97/2  # 最大可用半径
        self.area_total = self.r_total ** 2 * math.pi  # 最大可用面积
        self.n = n  # 孔的数量
        self.area_per_tube = self.area_total / self.n  # 平均面积
        self.r_avg = math.sqrt(self.area_per_tube / math.pi)  # 平均面积对应的半径

    def judge_prime(self):
        max_potential = math.ceil(math.sqrt(self.n))
        for i in range(2, max_potential):
            res = self.n / i
            if (res - int(res)) == 0:
                return True
            else:
                return False


if __name__ == "__main__":
    pass