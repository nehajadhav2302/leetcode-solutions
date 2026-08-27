from collections import deque
class Solution:
    def dfs(self, node, adj, visited, pathVis, check):
        visited[node] = 1
        pathVis[node] = 1

        for neigh in adj[node]:
            if not visited[neigh]:
                if self.dfs(neigh, adj, visited, pathVis, check) == True:
                    check[node] = 0
                    return True

            elif pathVis[neigh]:
                check[node] = 0
                return True

        check[node] = 1
        pathVis[node] = 0
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [0] * V
        pathVis = [0] * V
        check = [0] * V
        safeNodes = []

        for i in range(V):
            if not visited[i]:
                self.dfs(i, graph, visited, pathVis, check)
        
        for i in range(V):
            if check[i] == 1:
                safeNodes.append(i)
        
        return safeNodes