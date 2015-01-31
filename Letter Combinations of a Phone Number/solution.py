class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        maps = {}
        maps["2"] = "abc"
        maps["3"] = "def"
        maps["4"] = "ghi"
        maps["5"] = "jkl"
        maps["6"] = "mno"
        maps["7"] = "pqrs"
        maps["8"] = "tuv"
        maps["9"] = "wxyz"
        results = []
        ans = []
        self.backtrace(digits, maps, results, ans, 0)
        return results
    def backtrace(self, digits, maps, results, ans, pos):
        if len(ans) == len(digits):
            results.append("".join(ans))
            return
        for i in range(pos, len(digits)):
            char = digits[i]
            for j in range(0, len(maps[char])):
                ans.append(maps[char][j])
                self.backtrace(digits, maps, results, ans, i + 1)
                ans.pop()       