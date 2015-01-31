class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) <= 0:
            return num
        result = []
        ans = []
        visit = [False] * len(num)
        self.dfs(num, result, ans, visit)
        return result
    def dfs(self, num, result, ans, visit):
        if len(ans) == len(num):
            result.append(ans)
            return
        for i in range(0, len(num)):
            if visit[i] == False:
                ans.append(num[i])
                visit[i] = True
                self.dfs(num, result, ans[0:len(ans)], visit)
                visit[i] = False
                ans.pop()