from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ori_index, ori_num in enumerate(nums):
            j = hashmap.get(target - nums[ori_index])
            if j is not None:
                return [j, ori_index]
            hashmap[ori_num] = ori_index








print(Solution().twoSum([3, 8, 7, 2], 10))
