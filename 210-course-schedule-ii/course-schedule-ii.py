from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            adj[u].append(v)
        
        indegree = [0] * numCourses
        for i in range(numCourses):
            for neigh in adj[i]:
                indegree[neigh] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        path = []
        while q:
            node = q.popleft()
            path.append(node)

            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return path if len(path) == numCourses else []