class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        res = [0] * k
        curr = 1
        for cnt in range(k):
            tmp = curr % k
            if tmp == 0:
                return cnt+1
            elif res[tmp]:
                return -1
            else:
                res[tmp] = 1
                curr = 10 * tmp + 1
        return -1


if __name__ == '__main__':
    data = 3
    res = Solution().smallestRepunitDivByK(data)
    print(res)
