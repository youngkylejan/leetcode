class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) <= 0:
            return True
        i = 0
        while i < len(A) - 1:
            first = i + A[i]
            next = i + A[i]
            if next < len(A) and A[next] == 0:
                for j in range(i, i + A[i] + 1):
                    if j < len(A) and j + A[j] > first:
                        next = j + A[j]
                j = first
                for j in range(first, next + 1):
                    if j >= len(A):
                        return True
                    if A[j] != 0:
                        break
                if j == i:
                    return False
                i = j
            else:
                i = first
        return True