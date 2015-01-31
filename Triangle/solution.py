class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) <= 0:
            return 0
        dp = []
        for i in range(0, len(triangle)):
            row = []
            for j in range(0, len(triangle[i])):
                row.append(triangle[i][j])
            dp.append(row)
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j - 1 >= 0 and j < len(triangle[i - 1]):
                    dp[i][j] = min(dp[i - 1][j - 1] + dp[i][j], dp[i - 1][j] + dp[i][j])
                elif j - 1 < 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
        return sorted(dp[len(triangle) - 1])[0]