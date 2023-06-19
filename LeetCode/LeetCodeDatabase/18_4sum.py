class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 4:
            return res
        nums.sort()

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue

                lo = j+1
                hi = n-1
                tmp_sum_2 = nums[i] + nums[j]
                while lo < hi:
                    tmp_sum_4 = tmp_sum_2 + nums[lo] + nums[hi]
                    if tmp_sum_4 > target:
                        hi -= 1
                        continue
                    elif tmp_sum_4 < target:
                        lo += 1
                        continue

                    res.append([nums[i], nums[j], nums[lo], nums[hi]])

                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    hi -= 1

        return res







