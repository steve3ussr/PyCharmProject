class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # TODO
        n = len(nums)
        lo = 0
        hi = n-1
        res = [-1, -1]

        while lo <= hi:
            mid = (lo+hi)//2
            if target < nums[mid]:
                hi = mid-1  # hi >= target
            else:
                lo = mid+1
        res[0] = lo if 0 <= lo <= n-1 else -1

        lo = 0
        hi = n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1



if __name__ == '__main__':
    data = [5,7,7,8,8,10]
    target = 8
    res = Solution().searchRange(data, target)
    print(res)
