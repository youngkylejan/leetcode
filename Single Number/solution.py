class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for i in range(1, len(A)):
            result = A[i] ^ result
        return result