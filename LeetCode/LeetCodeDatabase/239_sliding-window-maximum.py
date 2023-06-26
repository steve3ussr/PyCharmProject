from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # init vars
        res = []
        lo = 0
        hi = k - 1
        window = deque()

        # init window
        _ = lo
        while _ <= hi:
            while window and window[-1][1] < nums[_]:
                window.pop()
            window.append([_, nums[_]])
            _ += 1
        print(f"WINDOW.init = {window}")

        # moving window
        while hi < len(nums):
            while window and window[0][0] < lo:
                window.popleft()
            while window and window[-1][1] < nums[hi]:
                window.pop()
            window.append([hi, nums[hi]])

            res.append(window[0][1])

            hi += 1
            lo += 1

        return res


if __name__ == '__main__':
    data = [1]
    res = Solution().maxSlidingWindow(data, 1)
    print(res)
