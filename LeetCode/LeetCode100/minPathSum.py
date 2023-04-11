class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        x = len(grid)
        y = len(grid[0])

        if x == 1:
            print(grid[0])
            return sum(grid[0])
        else:
            dp = []
            sum_ = 0
            for _ in range(y):
                dp.append(sum_ := sum_+grid[0][_])

        print(dp)

        for i in range(1, x):
            dp[0] = dp[0] + grid[i][0]
            if y > 1:
                for j in range(1, y):
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
                    print(f'min({dp[j]}, {dp[j - 1]}) + {grid[i][j]} = {dp[j]}')
            print(dp)
        return dp[-1]

if __name__ == '__main__':
    res = Solution().minPathSum([[0]])
    print(res)

