class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_length = 0
        ans_left = None
        ans_right = None

        def extender(a_str, left, right):
            while True:
                if left < 0 or right == len(a_str) or a_str[left] != a_str[right]:
                    return left+1, right-left-1
                else:
                    left -= 1
                    right += 1

        for i in range(len(s)):
            l_local, length_local = extender(s, i, i)
            if length_local > ans_length:
                ans_left = l_local
                ans_length = length_local

            l_local, length_local = extender(s, i, i+1)
            if length_local > ans_length:
                ans_left = l_local
                ans_length = length_local

        return s[ans_left:ans_left + ans_length]


a_str = 'abbq'
#a_str = 'cbbd'
#a_str = '1321344412'
res = Solution().longestPalindrome(a_str)
print(res)