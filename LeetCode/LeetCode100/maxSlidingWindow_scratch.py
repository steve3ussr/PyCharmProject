from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        q = []
        ans = []

        def monoAppend(new):
            while q and nums[new] >= nums[q[-1]]:
                q.pop()
            q.append(new)

        for i in range(k):
            monoAppend(i)
        ans.append(nums[q[0]])

        for i in range(k, len(nums)):
            monoAppend(i)
            while q[0] < i-k+1:
                q.pop(0)
            ans.append(nums[q[0]])

        return ans

if __name__ == '__main__':
    test_list = [1, 3, 10, 4, 8, 6, 7, 8, 9, 0]
    res = Solution().maxSlidingWindow(test_list, 3)
    print(res)
