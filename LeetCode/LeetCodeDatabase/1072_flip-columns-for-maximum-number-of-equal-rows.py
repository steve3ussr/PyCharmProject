from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            if row[0]:
                cnt[tuple(row[1:])] += 1
            else:
                for i in range(len(row)):
                    row[i] ^= 1
                cnt[tuple(row[1:])] += 1
        return max(cnt.values())

if __name__ == '__main__':
    data = [1,3,3,3,2,2,2]
    res = Solution().maxEqualRowsAfterFlips(data)
    print(res)