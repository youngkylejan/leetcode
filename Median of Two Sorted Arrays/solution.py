class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if (m + n) % 2 == 0:
            return float((self.binarysearch(A, m, B, n, (m + n) / 2) + self.binarysearch(A, m, B, n, (m 
+ n) / 2 + 1))) / 2
        else:
            return self.binarysearch(A, m, B, n, (m + n) / 2 + 1)
    def binarysearch(self, A, m, B, n, k):
        if m <= 0:
            return B[k - 1]
        if n <= 0:
            return A[k - 1]
        if k <= 1:
            return min(A[0], B[0])
        if A[m / 2] >= B[n / 2]:
            if (m / 2 + n / 2 + 1) >= k:
                return self.binarysearch(A, m/2, B, n, k)
            else:
                return self.binarysearch(A, m, B[n/2+1:n], n - n/2 - 1, k - n/2 - 1)
        else:
            if (m / 2 + n / 2 + 1) >= k:
                return self.binarysearch(A, m, B, n/2, k)
            else:
                return self.binarysearch(A[m/2+1:m], m - m/2 - 1, B, n, k - m/2 - 1)