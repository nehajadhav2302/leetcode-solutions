class Solution:
    def dfs(self, row, col, grid, visited, d_row, d_col, n, m):
        visited[row][col] = 1

        for i in range(4):
            nrow = row + d_row[i]
            ncol = col + d_col[i]

            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and visited[nrow][ncol] == 0:
                self.dfs(nrow, ncol, grid, visited, d_row, d_col, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        total = 0

        d_row = [-1, 0, 1, 0]
        d_col = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    total += 1
                    self.dfs(i, j, grid, visited, d_row, d_col, n, m)
        return total