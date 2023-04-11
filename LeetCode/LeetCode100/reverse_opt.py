class Solution:
    def reverse(self, x: int) -> int:
        ans_max = (2**31 - 1) // 10
        ans_min = -2**31//10 + 1
        b = abs(x)
        ans = 0
        while True:
            if ans_min <= ans <= ans_max:
                ans = b % 10 + ans * 10
            else:
                return 0

            if b // 10 == 0:
                break
            else:
                b = b // 10

        return ans if x > 0 else -ans


test_int = -2147483641
res = Solution().reverse(test_int)
print(res)
