from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        V = 0
        max_height = max(height)
        while left != right:
            temp = (right - left) * min(height[left], height[right])
            V = max(V, temp)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return V
