class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if len(matrix) <= 0:
            return matrix
        matrix.reverse()
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j] = matrix[i][j] ^ matrix[j][i]
                matrix[j][i] = matrix[i][j] ^ matrix[j][i]
                matrix[i][j] = matrix[i][j] ^ matrix[j][i]
        return matrix