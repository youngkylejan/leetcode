class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l3 + 1) for row in range(l3 + 1)]
        dp[0][0] = True
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if i + j - 1 < len(s3):
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 
1] == s3[i + j - 1])
        return dp[l1][l2]