from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return ans
        else:
            nums.sort()

        nums_1 = None

        for i in range(len(nums)-2):
            if nums[i] > 0 or nums[i] == nums_1:
                continue
            nums_2 = nums_3 = None

            index_l = i+1
            index_r = len(nums)-1
            target = -nums[i]
            while index_l < index_r:
                temp_sum = nums[index_l] + nums[index_r]
                if temp_sum < target:
                    index_l += 1
                elif temp_sum > target:
                    index_r -= 1
                else:

                    if nums_2 == nums[index_l] and nums_3 == nums[index_r]:
                        index_l += 1
                        index_r -= 1
                        continue
                    else:
                        ans.append([nums_1 := nums[i], nums_2 := nums[index_l], nums_3 := nums[index_r]])

        return ans


test_list = [0,0,0,0,0,0,0]
res = Solution().threeSum(test_list)
print(res)
