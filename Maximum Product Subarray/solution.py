class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        dp = [0] * len(A)
        for i in range(0, len(A)):
            dp[i] = A[i]
        positive = A[0]
        negative = A[0]
        product = A[0]
        for i in range(1, len(A)):
            if A[i] < 0:
                positive = positive ^ negative
                negative = positive ^ negative
                positive = positive ^ negative
            positive = max(A[i], positive * A[i])
            negative = min(A[i], negative * A[i])
            product = max(positive, product)
        return product