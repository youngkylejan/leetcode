class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if len(p) - p.count('*') > len(s):
            return False
        dp = [False] * (len(p) + 1)
        dp[0] = True
        for j in range(0, len(p)):
            dp[j + 1] = dp[j] and p[j] == '*'
        for i in range(0, len(s)):
                        newdp = [False] * (len(p) + 1)
            for j in range(0, len(p)):
                if p[j] != '*':
                    newdp[j + 1] = dp[j] and (s[i] == p[j] or p[j] == '?')
                else:
                    newdp[j + 1] = dp[j + 1] or newdp[j]
            dp = newdp[::]
        return dp[len(p)]