class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # TODO
        res_left = -1
        res_right = -1

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if

        left = 0
        right = len(nums) - 1
        while left <= right:
            pass


if __name__ == '__main__':
    data = [5,7,7,8,8,10]
    target = 8
    res = Solution().searchRange(data, target)
    print(res)
