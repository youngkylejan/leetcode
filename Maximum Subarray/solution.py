class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) <= 0:
            return 0
        maxNum = A[0]
        dp = [0] * len(A)
        for i in range(0, len(A)):
            dp[i] = A[i]
        for i in range(1, len(A)):
            dp[i] = dp[i - 1] + dp[i] if dp[i - 1] + dp[i] > dp[i] else dp[i]
            if dp[i] > maxNum:
                maxNum = dp[i]
        return maxNum