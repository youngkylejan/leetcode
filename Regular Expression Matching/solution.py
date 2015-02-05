class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for row in range(m + 1)]
        dp[0][0] = True
        for i in range(0, m):
            dp[i + 1][0] = False
        for j in range(0, n):
            dp[0][j + 1] = j > 0 and p[j] == '*' and dp[0][j - 1]
        for i in range(0, m):
            for j in range(0, n):
                if p[j] != '*':
                    dp[i + 1][j + 1] = dp[i][j] and (s[i] == p[j] or p[j] == '.')
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j - 1] and j > 0 or dp[i + 1][j] or dp[i][j + 1] and j > 0 and (s[i] == p[j - 1] or p[j - 1] == '.')
        return dp[m][n]