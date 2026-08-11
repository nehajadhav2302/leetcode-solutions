from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        total = 0
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mins = 0

        while q:
            k = len(q)
            count += k

            for _ in range(k):
                x, y = q.popleft()

                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 1:
                        continue
                    
                    grid[nx][ny] = 2
                    q.append((nx, ny))
            
            if q:
                mins += 1
            
        return mins if total == count else -1