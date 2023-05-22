class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stk = []
        ans = [-1] * n

        for i in range(2*n-1):
            j = i % n
            while stk and nums[stk[-1]] < nums[j]:
                ans[stk.pop()] = nums[j]
            stk.append(j)

        print(ans)


if __name__ == '__main__':
    data = [4, 1, 2]
    res = Solution().nextGreaterElements(data)
    print(res)
