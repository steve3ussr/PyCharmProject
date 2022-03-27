class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        k = 2 * numRows - 2
        ans = []

        for i in range(numRows):
            ans.append('')
        for i, v in enumerate(s):
            temp = i % k
            a = temp if temp < numRows else k - temp
            ans[a] += v

        return ''.join(ans)


test_list = "PAYPALISHIRING"

r = 3
res = Solution().convert(test_list, r)
print(res)
