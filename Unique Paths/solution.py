class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[0] * n for row in range(m)]
        dp[0][0] = 1
        for i in range(0, m):
            if i + 1 < m:
                dp[i + 1][0] = dp[i][0]
        for j in range(0, n):
            if j + 1 < n:
                dp[0][j + 1] = dp[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j] + dp[i][j - 1])
        return dp[m - 1][n - 1]