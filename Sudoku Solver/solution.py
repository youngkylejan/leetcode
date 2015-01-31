class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        tmp = board[i][::]
                        board[i] = board[i][0:j] + [str(k)] + board[i][j+1:len(board[i])]
                        if self.isValidSudoku(board, i, j) == True:
                            if self.solveSudoku(board):
                                return True
                        board[i] = tmp[::]
                        del tmp
                    return False 
        return True
    def isValidSudoku(self, board, row, col):
        for i in range(0, 9):
            if i != row and board[row][col] == board[i][col]:
                return False
        for j in range(0, 9):
            if j != col and board[row][col] == board[row][j]:
                return False
        for i in range((row/3)*3, (row/3+1)*3):
            for j in range((col/3)*3, (col/3+1)*3):
                if i != row and j!= col and board[row][col] == board[i][j]:
                    return False
        return True