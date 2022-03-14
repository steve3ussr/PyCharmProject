'''
给定一个整数数组 nums和一个整数目标值 target，
请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以按任意顺序返回答案。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 判断nums长度
        if len(nums) < 2:
            print("真短")
            return
        # main
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    sorted([i, j])
                    print(
                        f"数组中的第{i+1}个元素：{nums[i]}，和第{j+1}个元素：{nums[j]}，相加等于{target}"
                    )
                    return [i, j]
        print('找不到，根本就没有')
        '''
        nums_rebuild = [abs(i - target / 2) for i in nums]
        nums_rebuild.sort()

        def lookup(a_list):
            for k in range(len(nums_rebuild) - 1):
                if nums_rebuild[k] == nums_rebuild[k + 1]:
                    return k
            print("?")
            return

        while True:
            try:
                wanted_index_0 = lookup(nums_rebuild)
                value_1 = int(nums_rebuild[wanted_index_0] + target / 2)
                value_2 = int(target / 2 - nums_rebuild[wanted_index_0])
                index_1 = nums.index(value_1)
                index_2 = nums.index(value_2)
                if index_1 == index_2:
                    index_2 = nums.index(value_2, index_1+1)
                if nums[index_1] + nums[index_2] == target:
                    wanted_index = [index_1, index_2]
                    wanted_index.sort()
                    return wanted_index
                else:
                    nums_rebuild = nums_rebuild[wanted_index_0 + 1:]
            except ValueError:
                nums_rebuild = nums_rebuild[wanted_index_0+1:]


print(Solution().twoSum([2,3,11, 8, 3, 8, 7, 3, 7,2, 15, 2, 2, 11,15], 9))
