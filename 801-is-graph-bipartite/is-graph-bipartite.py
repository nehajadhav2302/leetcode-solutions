from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                q = deque([i])
                color[i] = 0

                while q:
                    u = q.popleft()

                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            q.append(v)
                        
                        elif color[u] == color[v]:
                            return False
        return True