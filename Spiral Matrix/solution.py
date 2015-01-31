class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) <= 0:
            return []
        result = []
        m = len(matrix)
        n = len(matrix[0])
        visit = [[False] * n for row in range(m)]
        rowUp = 0
        rowDown = m
        lineLeft = 0
        lineRight = n
        while len(result) < m * n:
            for j in range(lineLeft, lineRight):
                if visit[rowUp][j] == False:
                    result.append(matrix[rowUp][j])
                    visit[rowUp][j] = True
            rowUp = rowUp + 1
            for i in range(rowUp, rowDown):
                if visit[i][lineRight - 1] == False:
                    result.append(matrix[i][lineRight - 1])
                    visit[i][lineRight - 1] = True
            lineRight = lineRight - 1
            for j in range(lineRight - 1, lineLeft - 1, -1):
                if visit[rowDown - 1][j] == False:  
                    result.append(matrix[rowDown - 1][j])
                    visit[rowDown - 1][j] = True
            rowDown = rowDown - 1
            for i in range(rowDown - 1, rowUp - 1, -1):
                if visit[i][lineLeft] == False:
                    result.append(matrix[i][lineLeft])
                    visit[i][lineLeft] = True
            lineLeft = lineLeft + 1
        return result