class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = hi = 0
        for hi in range(len(nums)):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
        return nums



if __name__ == '__main__':
    data = [1,0,12]
    res = Solution().moveZeroes(data)
    print(res)
