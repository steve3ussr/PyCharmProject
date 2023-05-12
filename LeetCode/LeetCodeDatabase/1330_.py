class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(n - 1):
            s += abs(nums[i] - nums[i + 1])
        print(s)
        exchange = [None, None]
        ma = 0


        for l in range(n - 1):
            for r in range(l + 1, n):
                if l == 0 and r != (n-1):
                    tmp = s - abs(nums[r] - nums[r+1]) + abs(nums[l] - nums[r+1])

                elif l != 0 and r == (n-1):
                    tmp = s - abs(nums[l] - nums[l-1]) + abs(nums[l-1] - nums[r])

                elif l != 0 and r != (n-1):
                    tmp = s - abs(nums[l] - nums[l-1]) + abs(nums[r] - nums[l-1]) - abs(nums[r] - nums[r+1]) + abs(nums[l] - nums[r+1])

                else:
                    pass
                print(f"tmp={tmp}, exchange={[l, r]}")
                if tmp > ma:
                    ma = tmp
                    exchange = [l, r]

        print(exchange)
        print(ma)






if __name__ == '__main__':
    data = [2,4,9,24,2,1,10]
    res = Solution().maxValueAfterReverse(data)
    print(res)
