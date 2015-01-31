class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) <= 0:
            return []
        result = []
        solution = []
        self.dfs(s, result, solution, 0)
        new = []
        for item in result:
            temp = "".join(item)
            if len(temp) == len(s):
                new.append(item)
        return new
    def dfs(self, s, result, solution, start):
        if start == len(s):
            result.append(solution)
            return
        for i in range(start, len(s)):
            if s[start:i + 1] == s[start:i + 1][::-1]:
                solution.append(s[start:i + 1])
                self.dfs(s, result, solution[0:len(solution)], i + 1)
                solution.pop()