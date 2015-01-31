class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) <= 0 or obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len
(obstacleGrid[0]) - 1] == 1:
            return 0
        dp = [[0] * (len(obstacleGrid[0])) for row in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j] + dp[i][j - 1])
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]