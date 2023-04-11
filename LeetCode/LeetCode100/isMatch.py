class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        p_str = []
        p_status = []

        i = 0
        while True:
            try:
                if p[i + 1] == '*':
                    p_str.append(p[i])
                    p_status.append(1)
                    i += 2
                else:
                    p_str.append(p[i])
                    p_status.append(0)
                    i += 1
            except IndexError:  # 已经是最后一个所以读不到i+1，或者已经超过边界所以读不到i
                try:  # 已经是最后一个所以读不到i+1
                    p_str.append(p[i])
                    p_status.append(0)
                except IndexError:  # 已经超过边界所以读不到i
                    pass
                finally:
                    break

        print(p_str)
        print(p_status)

        def match(a: int, b: int) -> bool:
            if a == 0:
                if p_status[b-1] == 1:
                    return False
                elif p_str[b-1] == '.':
                    return True
                else:
                    return False
            else:
                if s[a-1] == p_str[b-1] or p_str[b-1] == '.':
                    return True
                else:
                    return False

        m = len(s)
        n = len(p_str)
        dp = [[False for i in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(1, n+1):
                if p_status[j-1] == 0:
                    dp[i][j] = dp[i-1][j-1] and match(i, j)
                else:
                    if match(i, j):
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]
        print(dp)
        return dp[m][n]


test_str = "aa"
regular_str = "ab*a*"
res = Solution().isMatch(test_str, regular_str)
print(res)
