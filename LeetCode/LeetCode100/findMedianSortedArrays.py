class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def findmid(list1, list2, k):
            if not list1:  # nums1 = []
                return list2[k-1]
            elif not list2:  # nums2 = []
                return list1[k-1]
            elif k == 1:
                return min(list1[0], list2[0])

            else:
                pass

            if len(list1) < k//2:
                a = len(list1)
                b = k - a
            elif len(list2) < k//2:
                b = len(list2)
                a = k - b
            else:
                a = b = k // 2

            if list1[a - 1] >= list2[b - 1]:
                list2 = list2[b:]
                k -= b
            else:
                list1 = list1[a:]
                k -= a
            print(list1, list2, k)
            return findmid(list1, list2, k)

        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2:
            t1 = t2 = (m + n) // 2+1
        else:
            t1 = (m + n) // 2+1
            t2 = t1 - 1
        print(t1, t2)
        v1 = findmid(k1 := nums1, k2 := nums2, t1)
        v2 = findmid(k1 := nums1, k2 := nums2, t2)
        print(v1, v2)
        return (v1 + v2) / 2


a = [1]
b = [2, 3]
mid = Solution().findMedianSortedArrays(a, b)
print(mid)
