from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        visited = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append((i, j, 0))
        
        d_row = [0, 1, 0, -1]
        d_col = [1, 0, -1, 0]

        while q:
            row, col, steps = q.popleft()
            dist[row][col] = steps

            for i in range(4):
                nrow = row + d_row[i]
                ncol = col + d_col[i]

                if 0 <= nrow < m and 0 <= ncol < n and not visited[nrow][ncol]:
                    q.append((nrow, ncol, steps + 1))
                    visited[nrow][ncol] = 1
        return dist