class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.binarysearch(A, target, 0, len(A) - 1)
    def binarysearch(self, A, target, start, end):
        if start > end:
            return start
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.binarysearch(A, target, start, mid - 1)
        else:
            return self.binarysearch(A, target, mid + 1, end)