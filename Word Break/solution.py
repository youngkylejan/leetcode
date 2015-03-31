class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) <= 0:
            return False
        start = 0
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j+1] in dict and dp[j + 1] == True:
                    dp[i] = True
        return dp[0]
