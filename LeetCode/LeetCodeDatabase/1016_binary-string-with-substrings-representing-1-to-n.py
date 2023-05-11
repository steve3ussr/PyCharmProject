class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # return True if len(s)*(len(s)+1)/2 >= n and all([bin(i)[2:] in s for i in range(1, n+1)]) else False
        if len(s) * (len(s) + 1) / 2 >= n:
            pass
        else:
            return False

        for i in range(1, n + 1):
            res = bin(i)[2:]
            if res in s:
                pass
            else:
                return False
        return True


if __name__ == '__main__':
    res = Solution().queryString('0110', 3)
    print(res)
