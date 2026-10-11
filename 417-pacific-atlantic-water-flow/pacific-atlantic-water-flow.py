class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return 0
        
        n, m = len(heights), len(heights[0])
        pacific = [[0] * m for _ in range(n)]
        atlantic = [[0] * m for _ in range(n)]

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(row, col, visited):
            visited[row][col] = 1

            for x, y in directions:
                nrow = row + x
                ncol = col + y

                if 0 <= nrow < n and 0 <= ncol < m and heights[row][col] <= heights[nrow][ncol] and visited[nrow][ncol] == 0:
                    dfs(nrow, ncol, visited)
        
        #First row
        for i in range(m):
            if not pacific[0][i]:
                dfs(0, i, pacific)
        
        #First col
        for i in range(n):
            if not pacific[i][0]:
                dfs(i, 0, pacific)

        #Last row
        for i in range(m):
            if not atlantic[n - 1][i]:
                dfs(n - 1, i, atlantic)
        
        #Last col
        for i in range(n):
            if not atlantic[i][m - 1]:
                dfs(i, m - 1, atlantic)
        
        result = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result
        