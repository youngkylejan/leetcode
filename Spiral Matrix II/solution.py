class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def generateMatrix(self, n):
        if n <= 0:
            return []
        matrix = [[0] * n for row in range(n)]
        rowUp = 0
        rowDown = n
        lineLeft = 0
        lineRight = n
        num = 1
        while num <= n * n:
            for j in range(lineLeft, lineRight):
                if matrix[rowUp][j] == 0:
                    matrix[rowUp][j] = num
                    num = num + 1
            rowUp = rowUp + 1
            for i in range(rowUp, rowDown):
                if matrix[i][lineRight - 1] == 0:
                    matrix[i][lineRight - 1] = num
                    num = num + 1
            lineRight = lineRight - 1
            for j in range(lineRight - 1, lineLeft - 1, -1):
                if matrix[rowDown - 1][j] == 0:
                    matrix[rowDown - 1][j] = num
                    num = num + 1
            rowDown = rowDown - 1
            for i in range(rowDown - 1, rowUp - 1, -1):
                if matrix[i][lineLeft] == 0:
                    matrix[i][lineLeft] = num
                    num = num + 1
            lineLeft = lineLeft + 1
                    return matrix