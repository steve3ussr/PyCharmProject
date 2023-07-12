from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums

        window = deque()
        for i in range(k):
            while window and window[-1][1] < nums[i]:
                window.pop()
            window.append([i, nums[i]])

        lo = 1
        hi = k
        res = [window[0][1]]
        while hi < len(nums):
            if window and window[0][0] < lo:
                window.popleft()
            while window and window[-1][1] < nums[hi]:
                window.pop()
            window.append([hi, nums[hi]])
            res.append(window[0][1])
            lo += 1
            hi += 1
        return res


if __name__ == '__main__':
    data = [1]
    res = Solution().maxSlidingWindow(data, 1)
    print(res)
