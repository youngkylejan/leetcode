class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        p = 0
        q = p + 1
        count = 0
        while q < len(A):
            if A[p] == A[q]:
                count = count + 1
            else:
                count = 0
            if count == 2:
                del A[q]
                count = count - 1
                continue
            p = p + 1
            q = q + 1
        return len(A)