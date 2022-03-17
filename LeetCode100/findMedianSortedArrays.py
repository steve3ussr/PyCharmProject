class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def insert(num, list_, start, end):
            if start == end:
                if num <= list_[start]:
                    list_.insert(start, num)
                else:
                    list_.insert(start + 1, num)
                return
            else:  # length//2 >= 1
                length = end - start + 1
                if num > list_[start + length // 2 - 1]:
                    return insert(num, list_, start + length // 2, end)
                else:
                    return insert(num, list_, start, start + length // 2 - 1)

        def mid_num(a_list):
            if len(a_list) % 2 > 0:
                return a_list[(len(a_list) // 2)]
            else:
                return (a_list[len(a_list) // 2] + a_list[len(a_list) // 2 - 1]) / 2

        if len(nums1) == 0:
            return mid_num(nums2)
        elif len(nums2) == 0:
            return mid_num(nums1)
        else:
            for var_ in nums2:
                insert(var_, nums1, 0, len(nums1)-1)

        print(nums1)
        return mid_num(nums1)


a = [1]
b = []
mid = Solution().findMedianSortedArrays(a, b)
print(mid)
