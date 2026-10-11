class Solution:
    def dfs(self, row, col, n, m, visited, grid, d_row, d_col):
        visited[row][col] = 1
        area = 1
        
        for i in range(4):
            nrow = row + d_row[i]
            ncol = col + d_col[i]

            if 0 <= nrow < n and 0 <= ncol < m and visited[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                area += self.dfs(nrow, ncol, n, m, visited, grid, d_row, d_col)
        return area

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        max_area = 0

        d_row = [0, 1, 0, -1]
        d_col = [1, 0, -1, 0]

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    area = self.dfs(i, j, n, m, visited, grid, d_row, d_col)
                    max_area = max(max_area, area)
        
        return max_area