import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        effort = [[float('inf')] * m for _ in range(n)]

        d_row = [-1, 0, 1, 0]
        d_col = [0, 1, 0, -1]

        pq = []
        effort[0][0] = 0
        heapq.heappush(pq, (0, 0, 0))

        while pq:
            d, r, c = heapq.heappop(pq)

            if r == n - 1 and c == m - 1:
                return d
            
            for i in range(4):
                nrow = r + d_row[i]
                ncol = c + d_col[i]

                if 0 <= nrow < n and 0 <= ncol < m:
                    abs_diff = max(d, abs(heights[r][c] - heights[nrow][ncol]))
                    if abs_diff < effort[nrow][ncol]:
                        effort[nrow][ncol] = abs_diff
                        heapq.heappush(pq, (abs_diff, nrow, ncol))
                    
        return 0