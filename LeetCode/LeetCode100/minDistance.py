import pprint


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None for j in range(len(word2)+1)] for i in range(len(word1)+1)]


        for i in range(0, len(word1) + 1):
            for j in range(0, len(word2)+1):

                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:

                    tmp = 0 if word1[i-1] == word2[j-1] else 1
                    dp[i][j] = min(
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j-1] + tmp
                    )

        pprint.pprint(dp)
        return dp[-1][-1]

    def minDistanceBest(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = list(range(n+1))
        for i in range(m):
            left_up = dp[0]
            dp[0]= i+1
            for j in range(n):
                dp[j+1], left_up= min(dp[j]+1, dp[j+1]+1, left_up+(int(word1[i]!=word2[j]))), dp[j+1]
        return dp[-1]


if __name__ == '__main__':
    Solution().minDistance('12345', '123')