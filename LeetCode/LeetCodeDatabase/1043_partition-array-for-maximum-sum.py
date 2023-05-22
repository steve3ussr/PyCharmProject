from functools import cache
from math import inf


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        return self.v3_dp(arr, k)

    def v1_iter_simple(self, arr, k):
        def func(lst):
            if len(lst) <= k:
                return len(lst) * max(lst)

            ma = -inf
            for i in range(-1, -(k + 1), -1):
                lst_front = lst[:i]
                lst_rear = lst[i:]
                ma = max(ma, func(lst_front) + max(lst_rear) * len(lst_rear))

            return ma

        return func(arr)

    def v2_iter_cache(self, arr, k):
        @cache
        def func(length):
            if length <= k:
                return length * max(arr[:length])

            ma = 0
            for i in range(length-1, length-1-k, -1):
                lst_rear = arr[i:length]
                ma = max(ma, func(i) + max(lst_rear) * len(lst_rear))

            return ma

        return func(len(arr))

    def v3_dp(self, arr, k):
        n = len(arr)
        dp = [0] * (n+1)

        for i in range(1, n+1):
            if i <= k:
                dp[i] = i * max(arr[:i])
            else:
                ma = 0
                for j in range(1, k+1):
                    _ = arr[i-j:i]
                    ma = max(ma, arr[i-j])
                    dp[i] = max(dp[i], dp[i-j] + j * ma)

        print(dp)
        return dp[-1]

    def v4_dp_opt(self, arr, k):
        n = len(arr)
        f = [0] * k
        for i in range(n):
            res = mx = 0
            for j in range(i, max(i - k, -1), -1):
                mx = max(mx, arr[j])  # 一边枚举 j，一边计算子数组的最大值
                # 注意在循环结束前，f[(i+1)%k] 是需要用到的，不能提前覆盖
                res = max(res, f[j % k] + (i - j + 1) * mx)
            f[(i + 1) % k] = res
        return f[n % k]


if __name__ == '__main__':
    data = [1, 15, 7, 9, 2, 5, 10]
    num = 3
    res = Solution().maxSumAfterPartitioning(data, num)
    print(res)
