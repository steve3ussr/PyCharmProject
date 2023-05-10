from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        return self.v2(nums)

    def v1(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            ma = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    ma = max(ma, dp[j])

            dp[i] += ma

        return max(dp)

    def v2(self, nums):
        g = []
        for num in nums:
            j = bisect_left(g, num)
            if j == len(g):
                g.append(num)
            else:
                g[j] = num

        return len(g)



if __name__ == '__main__':
    data = [0,1,0,3,2,3]
    res = Solution().lengthOfLIS(data)
    print(res)
