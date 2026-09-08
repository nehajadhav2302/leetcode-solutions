import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dist = [float('inf')] * n
        ways = [0] * n
        pq = []
        dist[0] = 0
        ways[0] = 1
        heapq.heappush(pq, (0, 0))

        mod = int(1e9 + 7)

        while pq:
            d, node = heapq.heappop(pq)

            for v, w in adj[node]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
                    ways[v] = ways[node]
                elif d + w == dist[v]:
                    ways[v] = (ways[v] + ways[node]) % mod
        return ways[n - 1] % mod