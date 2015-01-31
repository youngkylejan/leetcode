class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return self.binarysearch(x, 0, x)
    def binarysearch(self, x, start, end):
        if start > end:
            return start - 1
        mid = (start + end) / 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            return self.binarysearch(x, start, mid - 1)
        else:
            return self.binarysearch(x, mid + 1, end)