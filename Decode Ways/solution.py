class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) <= 0:
            return 0
        maps = {}
        tmp = 65
        for i in range(1, 27):
            maps[i] = chr(tmp)
            tmp = tmp + 1
        dp = [0] * (len(s) + 1)
        dp[0] = 0 if s[0] == '0' else 1
        dp[1] = 0 if s[0] == '0' else 1
        j = 2
        for i in range(1, len(s)):
            if s[i] == '0' and int(s[i - 1]) * 10 + int(s[i]) not in maps:
                return 0
            if s[i] == '0' and int(s[i - 1]) * 10 + int(s[i]) in maps:
                dp[j] = dp[j - 2]
            elif s[i - 1] == '0':
                dp[j] = dp[j - 1]
            else:
                dp[j] = dp[j - 1] + dp[j - 2] if int(s[i - 1]) * 10 + int(s[i]) in maps else dp[j - 1]
            j = j + 1
        return dp[j - 1]