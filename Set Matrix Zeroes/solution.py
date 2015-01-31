class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix) <= 0:
            return matrix
        visit = [[False] * len(matrix[0]) for row in range(len(matrix))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if visit[i][j] == False and matrix[i][j] == 0:
                    row = i
                    for k in range(0, len(matrix[0])):
                        if k != j and matrix[row][k] == 0:
                            continue
                        matrix[row][k] = 0
                        visit[row][k] = True
                    column = j
                    for t in range(0, len(matrix)):
                        if t != i and matrix[t][column] == 0:
                            continue
                        matrix[t][column] = 0
                        visit[t][column] = True
                elif visit[i][j] == True:
                    continue