class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) <= 0:
            return False
        result = []
        ans = ""
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        self.backtrace(s, dict, result, ans, len(s) - 1, dp)
        return result
    def backtrace(self, s, dict, result, ans, end, dp):
        if end == -1 and dp[0] == True:
            result.append(ans);
            return
        for i in range(end, -1, -1):
            for j in range(i, end + 1):
                if s[i:j + 1] in dict and dp[j + 1] == True:
                    dp[i] = True
                    self.backtrace(s, dict, result, s[i:j + 1] + " " + ans if ans != "" else s[i:j + 1], 
i - 1, dp)
                    dp[i] = False