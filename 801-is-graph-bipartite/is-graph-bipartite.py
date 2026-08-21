class Solution:
    def dfs(self, node, col, graph, color):
        color[node] = col

        for i in graph[node]:
            if color[i] == -1:
                if not self.dfs(i, col ^ 1, graph, color):
                    return False
            elif color[i] == col:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if not self.dfs(i, 0, graph, color):
                    return False
        return True