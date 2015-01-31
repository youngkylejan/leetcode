class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(word) <= 0:
            return False
        visit = [[False] * len(board[0]) for row in range(len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    result = self.dfs(board, word, visit, 0, i, j)
                    if result == True:
                        return True
        return False
    def dfs(self, board, word, visit, length, x, y):
        if length == len(word):
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        if visit[x][y] == False and board[x][y] == word[length]:
                        visit[x][y] = True
            if self.dfs(board, word, visit, length + 1, x + 1, y):
                return True
            if self.dfs(board, word, visit, length + 1, x - 1, y):
                return True
            if self.dfs(board, word, visit, length + 1, x, y + 1):
                return True
            if self.dfs(board, word, visit, length + 1, x, y - 1):
                return True
            visit[x][y] = False
                return False