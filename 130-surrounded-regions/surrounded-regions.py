class Solution:
    def dfs(self, row, col, board, visited, d_row, d_col):
        visited[row][col] = 1

        n,m = len(board), len(board[0])

        for i in range(4):
            nrow = row + d_row[i] 
            ncol = col + d_col[i]

            if 0 <= nrow < n and 0<= ncol < m and visited[nrow][ncol] == 0 and board[nrow][ncol] == 'O':
                self.dfs(nrow, ncol, board, visited, d_row, d_col)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        
        visited = [[0] * m for _ in range(n)]

        d_row = [-1, 0, 1, 0]
        d_col = [0, 1, 0, -1]

        for i in range(m):
            if board[0][i] == 'O' and visited[0][i] == 0:
                self.dfs(0, i, board, visited, d_row, d_col)
            
            if board[n - 1][i] == 'O' and visited[n - 1][i] == 0:
                self.dfs(n - 1, i, board, visited, d_row, d_col)
        
        for i in range(n):
            if board[i][0] == 'O' and visited[i][0] == 0:
                self.dfs(i, 0, board, visited, d_row, d_col)
            
            if board[i][m - 1] == 'O' and visited[i][m - 1] == 0:
                self.dfs(i, m - 1, board, visited, d_row, d_col)
        
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
        