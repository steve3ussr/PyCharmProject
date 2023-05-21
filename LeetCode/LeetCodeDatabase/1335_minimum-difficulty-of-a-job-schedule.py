from pprint import pprint as pp
from functools import cache
from math import inf
import operator
from itertools import accumulate


class Solution:

    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        self.dp_2d(jobDifficulty, d)
        self.dp_1d(jobDifficulty, d)

    def rec(self, data, d):
        n = len(data)
        if n < d:
            return -1

        lst_sum = list(accumulate(data, operator.add))
        lst_max = list(accumulate(data, max))

        @cache
        def _rec(i, day):
            # i 是任务个数，day 是天数
            if i == day:
                return lst_sum[i - 1]

            if day == 1:
                return lst_max[i - 1]

            max_ele = 0
            min_sum = inf
            for j in range(1, i + 2 - day):
                max_ele = max(max_ele, data[i - j])
                min_sum = min(min_sum, _rec(i - j - 1, day - 1) + max_ele)

            return min_sum

        return _rec(n, d)

    def dp_2d(self, data, d):
        n = len(data)

        if n < d: return -1

        lst_max = list(accumulate(data, max))
        lst_sum = list(accumulate(data, operator.add))

        if n == d: return lst_sum[-1]
        if d == 1: return lst_max[-1]

        dp = [[inf] * n for _ in range(d)]
        dp[0] = lst_max

        for i in range(1, d):
            dp[i][i] = lst_sum[i]
            for j in range(i + 1, n):

                max_ele = data[j]
                for k in range(j - 1, i - 2, -1):
                    max_ele = max(max_ele, data[k + 1])
                    dp[i][j] = min(dp[i][j], max_ele + dp[i - 1][k])

        pp(dp)
        return dp[-1][-1]

    def dp_1d(self, data, d):
        n = len(data)

        if n < d: return -1

        lst_sum = list(accumulate(data, operator.add))
        dp = list(accumulate(data, max))

        if n == d: return lst_sum[-1]
        if d == 1: return dp[-1]

        for i in range(1, d):
            for j in range(n - 1, i, -1):

                max_ele = data[j]
                dp[j] = inf
                for k in range(j - 1, i - 2, -1):
                    max_ele = max(max_ele, data[k + 1])
                    dp[j] = min(dp[j], max_ele + dp[k])
            dp[i] = lst_sum[i]

        pp(dp)
        return dp[-1]

    def monotonic_stack(self):
        pass


if __name__ == '__main__':
    data = [6, 5, 4, 3, 2, 1]
    day = 2
    res = Solution().minDifficulty(data, day)
    print(res)
