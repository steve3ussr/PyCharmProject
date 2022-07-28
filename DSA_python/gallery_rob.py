from pprint import pprint as pp


class Solution(object):
    def __init__(self, e):
        self.art_dict = {
            2: 3,
            3: 4,
            4: 5,
            5: 8,
            9: 10
        }
        self.dp = list([None for i in range(e+1)])
        self.dp[0] = 0
        self.dp[1] = 0
        self.e = e
        self.build_dp()

    def build_dp(self):
        for i in range(2, self.e + 1):
            self.dp[i] = max((self.dp[i - x] + self.art_dict[x] for x in self.art_dict if i >= x))


if __name__ == '__main__':
    inst = Solution(20)
    print(inst.dp)
