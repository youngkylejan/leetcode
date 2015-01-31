class Solution:
    def __init__(self):
        self.results = []
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        solution = []
        self.results = []
        self.DFS(candidates, target, solution, 0)
        return self.results
    def DFS(self, candidates, target, solution, next):
        if (target == 0):
            self.results.append(solution[:])
            return
        if ( next == len(candidates) or target - candidates[next] < 0):
            return
        solution.append(candidates[next])
        self.DFS(candidates, target - candidates[next], solution, next)
        solution.pop()
        self.DFS(candidates, target, solution, next + 1)