from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        visited = [[0] * m for _ in range(n)]
        dist = [[0] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited[i][j] = 1

        d_row = [-1, 0, 1, 0]
        d_col = [0, 1, 0, -1]
        
        while q:
            row, col, steps = q.popleft()
            dist[row][col] = steps

            for i in range(4):
                nrow = row + d_row[i]
                ncol = col + d_col[i]

                if 0 <= nrow < n and 0 <= ncol < m and visited[nrow][ncol] == 0:
                    q.append((nrow, ncol, steps + 1))
                    visited[nrow][ncol] = 1
        
        return dist