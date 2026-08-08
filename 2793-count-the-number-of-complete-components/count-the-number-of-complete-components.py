from collections import deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        component = 0

        for i in range(n):
            if not visited[i]:        
                q = deque()
                q.append(i)
                visited[i] = True

                nodes = 0
                edge_count = 0

                while q:
                    node = q.popleft()
                    nodes += 1
                    edge_count += len(adj[node])

                    for neighbour in adj[node]:
                        if not visited[neighbour]:
                            q.append(neighbour)
                            visited[neighbour] = True
                
                edge_count //= 2

                if edge_count == nodes * ( nodes - 1) // 2:
                    component += 1

        return component
