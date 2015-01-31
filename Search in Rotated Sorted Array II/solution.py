class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) <= 0:
            return False
        head = 0
        tail = len(A) - 1
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                tail = i - 1
                head = i
        if head == 0  and tail == len(A) - 1:
            return self.binarysearch(A, head, tail, target)
        else:
            r1 = self.binarysearch(A, 0, tail, target)
            r2 = self.binarysearch(A, head, len(A) - 1, target)
            return r1 if r1 == True else r2
    def binarysearch(self, A, start, end, target):
        if start > end:
            return False
        mid = (start + end) / 2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            return self.binarysearch(A, start, mid - 1, target)
        else:
            return self.binarysearch(A, mid + 1, end, target)