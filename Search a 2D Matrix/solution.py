class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        return self.search1(matrix, target, 0, len(matrix) - 1)
    def search1(self, matrix, target, start, end):
        if start > end:
            return False
        mid = (start + end) / 2
        edge = self.search2(matrix[mid], target, 0, len(matrix[mid]) - 1)
        if edge[0] == True:
            return True
        elif edge[1] == 0:
            return False
        elif edge[1] < 0:
            return self.search1(matrix, target, 0, mid - 1)
        else:
            return self.search1(matrix, target, mid + 1, end)
    def search2(self, row, target, start, end):
        if start > end:
            if target < row[0]:
                return [False, -1]
            elif target > row[len(row) - 1]:
                return [False, 1]
            else:
                return [False, 0]
        mid = (start + end) / 2
        if row[mid] == target:
            return [True, mid]
        elif row[mid] > target:
            return self.search2(row, target, start, mid - 1)
        else:
            return self.search2(row, target, mid + 1, end)