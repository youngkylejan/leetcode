class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A) <= 0:
            return 0
        ans = 0
        left = 0
        right = len(A) - 1
        maxLeft = 0
        maxRight = 0
        while left <= right:
            if A[left] <= A[right]:
                if A[left] >= maxLeft:
                    maxLeft = A[left]
                else:
                    ans = ans + maxLeft - A[left]
                left = left + 1
            else:
                if A[right] >= maxRight:
                    maxRight = A[right]
                else:
                    ans = ans + maxRight - A[right]
                right = right - 1
        return ans