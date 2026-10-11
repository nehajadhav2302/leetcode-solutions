class Solution:
    def dfs(self, row, col, n, m, board, visited, d_row, d_col):
        visited[row][col] = 1

        for i in range(4):
            nrow = row + d_row[i]
            ncol = col + d_col[i]

            if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == 'O' and visited[nrow][ncol] != 1:
                self.dfs(nrow, ncol, n, m, board, visited, d_row, d_col)

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        visited = [[0] * m for _ in range(n)]

        d_row = [0, 1, 0, -1]
        d_col = [1, 0, -1, 0]

        #First row
        for i in range(m):
            if board[0][i] == 'O' and visited[0][i] != 1:
                self.dfs(0, i, n, m, board, visited, d_row, d_col)
        
        #First col
        for i in range(n):
            if board[i][0] == 'O' and visited[i][0] != 1:
                self.dfs(i, 0, n, m, board, visited, d_row, d_col)
        
        #Last row
        for i in range(m):
            if board[n - 1][i] == 'O' and visited[n - 1][i] != 1:
                self.dfs(n - 1, i, n, m, board, visited, d_row, d_col)
        
        #Last col
        for i in range(n):
            if board[i][m - 1] == 'O' and visited[i][m - 1] != 1:
                self.dfs(i, m - 1, n, m, board, visited, d_row, d_col)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and visited[i][j] != 1:
                    board[i][j] = 'X'
    