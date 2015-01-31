class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if len(s) <= 0:
            return []
        result = []
        solution = ""
        self.backtracking(s, result, solution, 0, 0)
        return result
    def backtracking(self, s, result, solution, start, level):
        if len(solution) > len(s) + 4 or level > 4:
            return
        if len(solution) == len(s) + 4 and level == 4:
            result.append(solution[0:len(solution)-1])
            return
        if start > len(s):
            return
        for i in range(start, len(s)):
            if s[start:i+1] == "" or int(s[start:i+1]) > 255:
                break
            if s[start:i+1][0] == "0" and len(s[start:i+1]) > 1:
                continue
            self.backtracking(s, result, solution + s[start:i+1] + ".", i + 1,  level + 1)