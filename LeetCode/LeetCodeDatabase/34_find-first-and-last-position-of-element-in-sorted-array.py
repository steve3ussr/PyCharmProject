class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        res = [-1, -1]

        lo = 0
        hi = n-1

        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        if 0 <= lo < n and nums[lo] == target:
            res[0] = lo

        lo = 0
        hi = n-1

        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        if 0 <= hi < n and nums[hi] == target:
            res[1] = hi

        return res


if __name__ == '__main__':
    data = [5, 7, 7, 8, 8, 10]
    target = 8
    res = Solution().searchRange(data, target)
    print(res)
