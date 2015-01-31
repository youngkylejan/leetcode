class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        solution = []
        results = []
        self.DFS(candidates, target, solution, results, 0)
        return results
    def DFS(self, candidates, target, solution, results, next):
        if target == 0:
            results.append(solution[:])
            return
        if next == len(candidates) or target - candidates[next] < 0:
            return
        solution.append(candidates[next])
        self.DFS(candidates, target - candidates[next], solution, results, next + 1)
        temp = solution.pop()
        theta = 1
        while next + theta < len(candidates) and temp == candidates[next + theta]:
            theta = theta + 1
        self.DFS(candidates, target, solution, results, next + theta)