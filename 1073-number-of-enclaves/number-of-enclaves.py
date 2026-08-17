class Solution:
    def dfs(self, row, col, grid, visited, d_row, d_col):
        visited[row][col] = 1
        n, m = len(grid), len(grid[0])

        for i in range(4):
            nrow = row + d_row[i]
            ncol = col + d_col[i]

            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and visited[nrow][ncol] == 0 :
                self.dfs(nrow, ncol, grid, visited, d_row, d_col)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]

        d_row = [-1, 0, 1, 0]
        d_col = [0, 1, 0, -1]

        for i in range(m):
            if grid[0][i] == 1 and visited[0][i] == 0:
                self.dfs(0, i, grid, visited, d_row, d_col)
            if grid[n - 1][i] == 1 and visited[n - 1][i] == 0:
                self.dfs(n - 1, i, grid, visited, d_row, d_col)
        
        for i in range(n):
            if grid[i][0] == 1 and visited[i][0] == 0:
                self.dfs(i, 0, grid, visited, d_row, d_col)
            if grid[i][m - 1] == 1 and visited[i][m - 1] == 0:
                self.dfs(i, m - 1, grid, visited, d_row, d_col)
        
        count = 0

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    count += 1
        
        return count
        