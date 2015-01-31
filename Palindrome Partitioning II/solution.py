class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if len(s) <= 0:
            return
        dp = [0] * (len(s) + 1)
        for i in range(0, len(s) + 1):
            dp[i] = i - 1
        visit = [[False] * (len(s) + 1) for row in range(len(s) + 1)]
        for i in range(2, len(s) + 1):
            for j in range(i - 1, -1, -1):
                # print str(i) + " " + str(j)
                if s[j:i] == s[j:i][::-1] and (i - j - 1 < 2 or visit[j + 1][i - 1] == True):
                    visit[j][i] = True
                    dp[i] = min(dp[i], dp[j] + 1)
                # print dp
        return dp[len(s)]