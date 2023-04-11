class Solution:
    def baseNeg2(self, n: int) -> str:
        res = []
        while not 0 <= n <= 1:

            a = n // (-2)
            b = n % (-2)

            if b == -1:
                b = 1
                a += 1

            res.insert(0, str(b))
            n = a

        res.insert(0, str(n))

        return "".join(res)


if __name__ == '__main__':
    res = Solution().baseNeg2(14)
    print(res)
