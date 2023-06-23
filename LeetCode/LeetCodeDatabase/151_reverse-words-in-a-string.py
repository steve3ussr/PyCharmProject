class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        start = 0
        i = 0
        lst = []
        while i < n:
            if s[i] != ' ':
                start = i

                while i < n and s[i] != ' ':
                    i += 1
                lst.append(s[start:i])
            i += 1

        res = ""
        for v in reversed(lst):
            res += v
            res += ' '
        return res[:-1]

    """
    s = s.strip(' ')
    s = s.rstrip(' ')
    lst = s.split(' ')
    res = ""
    for v in lst[::-1]:
        res += v
        res += " "
    return res[:-1]    
    """

if __name__ == '__main__':
    print(Solution().reverseWords(' hello    world!   '))