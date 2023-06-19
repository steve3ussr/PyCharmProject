from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        dct = defaultdict(int)
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                dct[nums1[i] + nums2[j]] += 1

        res = 0
        for i in range(n):
            for j in range(n):
                res += dct[-nums3[i] - nums4[j]]

        return res
