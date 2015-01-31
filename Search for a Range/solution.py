class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        indexs = []
        self.binarysearch(A, target, indexs, 0, len(A) - 1)
        return indexs if len(indexs) > 0 else [-1, -1]
    def binarysearch(self, A, target, indexes, start, end):
        if start > end:
            return
        mid = (start + end) / 2
        if A[mid] == target:
            index1 = mid
            index2 = mid
            for i in range(mid, start - 1, -1):
                if A[i] == target:
                    index1 = i
                else:
                    break
            for j in range(mid, end + 1):
                if A[j] == target:
                    index2 = j
                else:
                    break
            indexes.append(index1)
            indexes.append(index2)
            return
        elif A[mid] > target:
            self.binarysearch(A, target, indexes, 0, mid - 1)
        else:
            self.binarysearch(A, target, indexes, mid + 1, end)