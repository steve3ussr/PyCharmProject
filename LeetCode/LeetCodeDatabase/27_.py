class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        hi = 0
        lo = 0
        while hi < len(nums):
            if nums[hi] == val:
                nums[lo] = nums[hi]
            else:
                lo += 1
            hi += 1

        return lo


if __name__ == '__main__':
    data = [1, 1, 4, 5, 1, 4]
    target = 4
    res = Solution().removeElement(data, target)
    print(res)
