class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        results = []
        ans = []
        self.backtrace(n, results, ans, 0, 0)
        return results
    def backtrace(self, n, results, ans, leftNum, rightNum):
        if leftNum < rightNum:
            return
        if leftNum == n and rightNum == n:
            results.append("".join(ans))
            return
        if leftNum > n:
            return
        ans.append("(")
        self.backtrace(n, results, ans, leftNum + 1, rightNum)
        ans.pop()
        ans.append(')')
        self.backtrace(n, results, ans, leftNum, rightNum + 1)
        ans.pop()