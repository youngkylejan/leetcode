class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        results = []
        solution = []
        self.DFS(n, k, solution, results, 1)
        return results
    def DFS(self, n, k, solution, results, num):
        if (len(solution) == k):
            results.append(solution[:])
            return
        if (num > n or len(solution) > k):
            return
        solution.append(num)
        self.DFS(n, k, solution, results, num + 1)
        solution.pop()
        self.DFS(n, k, solution, results, num + 1)