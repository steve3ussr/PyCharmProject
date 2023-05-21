from collections import Counter
from math import comb
from pprint import pprint


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return self.dp_2d(tiles)

    def dp_1d(self, tiles):

        dp = [0] * (1 + len(tiles))
        dp[0] = 1
        len_curr = 0
        for c in Counter(tiles).values():
            len_curr += c
            for l in range(len_curr, 0, -1):
                for k in range(1, min(l, c) + 1):
                    # dp[l] equals to dp[div-1][l]
                    # calc dp[div][l] don't need to calc it once more
                    dp[l] += dp[l - k] * comb(l, k)

        pprint(dp)
        return sum(dp[1:])

    def dp_2d(self, tiles):
        cnt = Counter(tiles).values()
        max_len = len(tiles)
        max_div = len(cnt)

        dp = [[0] * (1 + max_len) for _ in range(1 + max_div)]
        dp[0][0] = 1

        curr_len = 0
        for div, c in enumerate(cnt, 1):
            curr_len += c
            dp[div][0] = 1
            for l in range(1, 1 + curr_len):
                for k in range(min(l, c) + 1):
                    dp[div][l] += dp[div - 1][l - k] * comb(l, k)

        pprint(dp)
        return sum(dp[-1][1:])


if __name__ == '__main__':
    data = "AAABBC"
    res = Solution().numTilePossibilities(data)
    print(res)
