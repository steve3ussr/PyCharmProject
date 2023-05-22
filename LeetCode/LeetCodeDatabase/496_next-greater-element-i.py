class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dct = {v: -1 for v in nums1}
        stk = []

        for v in nums2:
            while stk and stk[-1] < v:
                _ = stk.pop()
                if _ in dct:
                    dct[_] = v
            stk.append(v)

        return list(dct.values())


if __name__ == '__main__':
    data_1 = [4, 1, 2]
    data_2 = [1, 3, 4, 2]
    res = Solution().nextGreaterElement(data_1, data_2)
    print(res)
