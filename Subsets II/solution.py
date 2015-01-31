class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result = []
        ans = []
        self.dfs(sorted(S), result, ans, 0)
        return result
    def dfs(self, S, result, ans, start):
        if start < len(S) + 1:
            result.append(sorted(ans))
        for i in range(start, len(S)):
            if i > start and S[i] == S[i - 1]:
                continue
            ans.append(S[i])
            self.dfs(S, result, ans[0:len(ans)], i + 1)
            ans.pop()