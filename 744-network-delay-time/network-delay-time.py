import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]: continue
            for v, w in adj[node]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        
        min_time = float('-inf')
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            min_time = max(min_time, dist[i])
        
        return min_time