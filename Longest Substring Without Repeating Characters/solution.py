class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 0:
            return 0
        hashs = {}
        ans = 0
        start = 0
        for i in range(0, len(s)):
            if (s[i] not in hashs.keys() or hashs[s[i]] < start) and i == len(s) - 1:
                ans = max(ans, i - start + 1)
            elif s[i] not in hashs.keys():
                hashs[s[i]] = i
            elif hashs[s[i]] < start:
                hashs[s[i]] = i
            else:
                ans = max(ans, i - start)
                start = hashs[s[i]] + 1
                hashs[s[i]] = i
        return ans