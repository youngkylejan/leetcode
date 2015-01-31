class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if len(S) <= 0:
            return []
        result = []
        ans = []
        self.dfs(S, result, ans, 0)
        return result
    def dfs(self, s, result, ans, start):
        if start <= len(s):
            result.append(sorted(ans))
        for i in range(start, len(s)):
            ans.append(s[i])
            self.dfs(s, result, ans[0:len(ans)], i + 1)
            ans.pop()