class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if len(grid) <= 0:
            return 0
        dp = [[0] * len(grid[0]) for row in range(len(grid))]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                dp[i][j] = grid[i][j]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j] + dp[i][j], dp[i][j - 1] + dp[i][j])
                elif i > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i][j]
        return dp[len(grid) - 1][len(grid[0]) - 1]