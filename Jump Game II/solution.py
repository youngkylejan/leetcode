class Solution:
    # @param A, a list of integers
    # @return a boolean
    def jump(self, A):
        maxReach = A[0]
        edge = 0
        step = 0
        for i in range(1, len(A)):
            if i > edge:
                step = step + 1
                edge = maxReach
                if edge > len(A) - 1:
                    return step
            maxReach = max(maxReach, A[i] + i)
        return step