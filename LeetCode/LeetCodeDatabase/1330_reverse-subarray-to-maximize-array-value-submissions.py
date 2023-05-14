class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(n - 1):
            s += abs(nums[i] - nums[i + 1])
        exchange = [None, None]
        ma = 0

        for l in range(n - 1):
            for r in range(l + 1, n):
                if l == 0 and r != (n - 1):
                    tmp = - abs(nums[r] - nums[r + 1]) + abs(nums[l] - nums[r + 1])

                elif l != 0 and r == (n - 1):
                    tmp = - abs(nums[l] - nums[l - 1]) + abs(nums[l - 1] - nums[r])

                elif l != 0 and r != (n - 1):
                    tmp = - abs(nums[l] - nums[l - 1]) + abs(nums[r] - nums[l - 1]) - abs(nums[r] - nums[r + 1]) + abs(
                        nums[l] - nums[r + 1])

                else:
                    pass

                if tmp > ma:
                    ma = tmp

        return s + ma

if __name__ == '__main__':
    data = [2,3,1,5,4]
    res = Solution().maxValueAfterReverse(data)
    print(res)
