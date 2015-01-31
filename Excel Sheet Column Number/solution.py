class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if len(s) <= 0:
            return 0
        maps = {}
        j = 1
        for i in range(ord('A'), ord('Z') + 1):
            maps[chr(i)] = j
            j = j + 1
        num = 26
        l = len(s)
        ans = 0
        for i in range(0, len(s)):
            ans = ans + pow(num, l - 1) * maps[s[i]]
            l = l - 1
        return ans