class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0, 1, 2]
        if n <= 2:
            return n
        else:
            a = 1
            b = 2
            for i in range(3, n+1):
                sum = a + b
                a = b
                b = sum

            return b


if __name__ == '__main__':
    Solution().climbStairs(5)
