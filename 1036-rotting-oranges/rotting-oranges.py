from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        d_row = [0, 1, 0, -1]
        d_col = [1, 0, -1, 0]

        while q and fresh > 0:
            k = len(q)

            for _ in range(k):
                x, y = q.popleft()

                for i in range(4):
                    nrow = x + d_row[i]
                    ncol = y + d_col[i]

                    if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        fresh -= 1
                        q.append((nrow, ncol))
            
            time += 1
        
        return time if fresh == 0 else -1
