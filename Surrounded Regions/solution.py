class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) <= 0:
            return
        zeroIndex = []
        visit = [[False] * len(board[0]) for row in range(len(board))]
        surrounded = [[False] * len(board[0]) for row in range(len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[i]) 
- 1):
                    zeroIndex.append([i, j])
                    visit[i][j] = False
                    surrounded[i][j] = False
                elif board[i][j] == "O":
                    surrounded[i][j] = True
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = collections.deque()
        for i in range(0, len(zeroIndex)):
            queue.append(zeroIndex[i])
            visit[zeroIndex[i][0]][zeroIndex[i][1]] = True
        while len(queue) > 0:
            front = queue.popleft()
            for item in move:
                nextX = front[0] + item[0]
                nextY = front[1] + item[1]
                if nextX < 0 or nextX >= len(board) or nextY < 0 or nextY >= len(board[0]):
                    continue
                if board[nextX][nextY] == "O" and visit[nextX][nextY] == False:
                    queue.append([nextX, nextY])
                    visit[nextX][nextY] = True
                    surrounded[nextX][nextY] = False
        for i in range(0, len(board)):
            line = ""
            for j in range(0, len(board[i])):
                if board[i][j] == "O" and surrounded[i][j] == True:
                    line = line + "X"
                else:
                    line = line + board[i][j]
            board[i] = line