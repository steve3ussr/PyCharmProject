class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if nums[0] >= 0:
            return [_ ** 2 for _ in nums]

        n = len(nums)

        if nums[-1] <= 0:
            return [nums[_]**2 for _ in range(n-1, -1, -1)]

        for i in range(n):
            if nums[i] >= 0:
                lo = i-1
                hi = i
                break

        res = []
        while True:
            if lo < 0 and hi >= n:
                return res
            elif lo < 0 and hi < n:
                res.extend([nums[_]**2 for _ in range(hi, n)])
                return res
            elif lo >= 0 and hi >= n:
                res.extend([nums[_]**2 for _ in range(lo, -1, -1)])
                return res

            if nums[lo] + nums[hi] >= 0:
                res.append(nums[lo]**2)
                lo -= 1
            else:
                res.append(nums[hi]**2)
                hi += 1


if __name__ == '__main__':
    data = [-1,2,2]
    res = Solution().sortedSquares(data)
    print(res)

