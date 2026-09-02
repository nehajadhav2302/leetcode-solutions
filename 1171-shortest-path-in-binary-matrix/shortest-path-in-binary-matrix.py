from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        dist = [[float('inf')] * n for _ in range(n)]
        q = deque([(1, 0, 0)])
        dist[0][0] = 1

        d_row = [-1, 0, 1, 0, -1, -1, 1, 1]
        d_col = [0, 1, 0, -1, -1, 1, -1, 1]

        while q:
            d, r, c = q.popleft()
            
            if r == n - 1 and c == n - 1:
                return d
            for i in range(8):
                nrow = r + d_row[i]
                ncol = c + d_col[i]

                if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == 0 and d + 1 < dist[nrow][ncol]:
                    dist[nrow][ncol] = d + 1
                    q.append((d + 1, nrow, ncol))
        return -1
                