class Solution:
    # @return an integer
    def romanToInt(self, s):
        ans = 0
        hashs = {}
        hashs['I'] = 1
        hashs['V'] = 5
        hashs['X'] = 10
        hashs['L'] = 50
        hashs['C'] = 100
        hashs['D'] = 500
        hashs['M'] = 1000
        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1:
                ans = ans + hashs[s[i]]
                continue
            if hashs[s[i]] >= hashs[s[i + 1]]:
                ans = ans + hashs[s[i]]
            else:
                ans = ans - hashs[s[i]]
        return ans