class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        res = n+1
        lo = hi = 0
        sum_curr = nums[0]

        while lo <= hi < n:
            print(f"curr_slice: {nums[lo:hi+1]}, sum={sum_curr}, lo={lo}, hi={hi}")
            if sum_curr >= target:

                res = min(res, hi-lo+1)
                if res == 1:
                    return res

                sum_curr -= nums[lo]
                lo += 1
            else:
                if hi+1 == n:
                    break
                else:
                    hi += 1
                    sum_curr += nums[hi]

        return res if res <= n else 0






if __name__ == '__main__':
    data = [1,2,3,4,5]
    target = 15
    res = Solution().minSubArrayLen(target, data)
    print(res)
