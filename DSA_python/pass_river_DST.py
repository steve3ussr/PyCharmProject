from pprint import pprint as pp


class Solution(object):
    def __init__(self, sheep, lion):
        self.sheep = sheep
        self.lion = lion
        self.dp = []
        for i in range(sheep + 1):
            temp = []
            for j in range(lion + 1):
                temp.append(None)
            self.dp.append(temp)
        # self.dp = list([list([None for j in range(lion+1)]) for i in range(sheep+1)])
        self.dp[sheep][lion] = 0
        self.move = [(1, 1), (1, 0), (0, 1), (2, 0), (0, 2)]
        self.possiblePath = []

    def judge_eat(self, x, y):
        """
        only judge after go and back
        """
        if x == 0 or x == self.sheep or x == y:
            return True
        else:
            return False

    def judge_index(self, x, y):
        """
        judge after go and back
        """
        return True if 0 <= x <= self.sheep and 0 <= y <= self.lion else False







if __name__ == '__main__':
    inst = Solution(3, 3)
    tmp = inst.passing_DST([(3, 3)])
    print(tmp)
    pp(inst.dp)

