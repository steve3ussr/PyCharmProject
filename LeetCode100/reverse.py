class Solution:
    def reverse(self, x: int) -> int:
        b = abs(x)
        ans = ''
        while True:
            ans += repr(b % 10)
            if b // 10 == 0:
                break
            else:
                b = b // 10

        ans = int(ans) if x > 0 else -int(ans)
        return ans if -2**31 < ans < 2**31-1 else 0


test_int = 15342364695458684354567898765432345678
res = Solution().reverse(test_int)
print(res)
