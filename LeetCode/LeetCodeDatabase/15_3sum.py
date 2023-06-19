class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        if n < 3:
            return res
        nums.sort()

        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo = i + 1
            hi = n - 1
            while lo < hi:
                tmp_sum = nums[i] + nums[lo] + nums[hi]
                if tmp_sum > 0:
                    hi -= 1
                    continue
                elif tmp_sum < 0:
                    lo += 1
                    continue

                res.append([nums[i], nums[lo], nums[hi]])

                while lo < hi and nums[lo] == nums[lo + 1]:
                    lo += 1
                lo += 1

                while lo < hi and nums[hi] == nums[hi - 1]:
                    hi -= 1
                hi -= 1

        return res

