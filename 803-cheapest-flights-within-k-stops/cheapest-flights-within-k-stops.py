from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        dist = [float('inf')] * n
        q = deque()
        q.append((0, src, 0))

        while q:
            stop, node, cost = q.popleft()

            if stop > k: continue
            for v, e_cost in adj[node]:
                if cost + e_cost < dist[v] and stop <= k:
                    dist[v] = cost + e_cost
                    q.append((stop + 1, v, dist[v]))
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]