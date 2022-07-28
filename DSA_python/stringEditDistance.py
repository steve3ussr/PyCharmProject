from pprint import pprint as pp


class Solution(object):
    def __init__(self, src, tgt):
        self.src = ' ' + src
        self.tgt = ' ' + tgt
        self.del_cost = 20
        self.ins_cost = 20
        self.dup_cost = 5
        self.dp = []
        self.dp_init()
        self.dp_build()

    def dp_init(self):
        for i in range(len(self.src)):
            tmp = []
            for j in range(len(self.tgt)):
                tmp.append(None)
            self.dp.append(tmp)

        for i in range(len(self.src)):
            self.dp[i][0] = self.del_cost * i

        for j in range(len(self.tgt)):
            self.dp[0][j] = self.ins_cost * j

    def dp_build(self):
        for i in range(1, len(self.src)):
            for j in range(1, len(self.tgt)):

                tmp = self.dup_cost if self.src[i] == self.tgt[j] else (self.del_cost + self.ins_cost)

                self.dp[i][j] = min(
                    self.dp[i-1][j] + self.del_cost,
                    self.dp[i][j-1] + self.ins_cost,
                    self.dp[i-1][j-1] + tmp,
                )


if __name__ == '__main__':
    inst = Solution('abcd', 'xzd')
    pp(inst.dp)
