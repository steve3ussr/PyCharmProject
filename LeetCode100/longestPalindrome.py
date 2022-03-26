class Solution:
    def longestPalindrome(self, s: str) -> (str, int, int):


        imax = 0
        jmax = 0
        length = 1
        i = 0
        while i <= len(s)-1:
            j = 0.5 if i % 1 else 1

            while True:
                if i-j < 0 or i+j == len(s):
                    break
                if s[int(i-j)] == s[int(i+j)]:
                    j += 1
                else:
                    break

            length_local = 2*j-1
            if 2*j-1 > length:
                jmax = j
                imax = i
                length = length_local

            i += 0.5

        return s[int(imax-jmax+1):int(imax+jmax)] if jmax != 0 else s[0]


a_str = 'aba'
#a_str = 'cbbd'
#a_str = '1321344412'
res = Solution().longestPalindrome(a_str)
print(res)
