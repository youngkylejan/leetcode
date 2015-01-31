class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if len(A) <= 0:
            return 1
        p = -1
        for i in range(0, len(A)):
            if A[i] > 0:
                p = p + 1
                self.swap(A, i, p)
        tmp = 0
        for i in range(0, p + 1):
            tmp = abs(A[i])
            if tmp <= p + 1:
                A[tmp - 1] = - abs(A[tmp - 1])
        ans = p + 1
        for i in range(0, p + 1):
            if A[i] > 0:
                ans = i
                break
        return ans + 1
    def swap(self, A, i, j):
        if i != j:
            A[i] = A[i] ^ A[j]
            A[j] = A[i] ^ A[j]
            A[i] = A[i] ^ A[j]