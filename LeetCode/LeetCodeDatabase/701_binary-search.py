import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.v1(nums, target)

    @staticmethod
    def v1(lst, k):
        n = len(lst)
        if n == 1:
            return -1 if lst[0] != k else 0

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if k > lst[mid]:
                left = mid + 1
            elif k < lst[mid]:
                right = mid - 1
            else:
                return mid

        return -1

    @staticmethod
    def v2(lst, k):
        pass


if __name__ == '__main__':
    data = [2, 5]
    target = 5
    res = Solution().search(data, target)
    print(res)
