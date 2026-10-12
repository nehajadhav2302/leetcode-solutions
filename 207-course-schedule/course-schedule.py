from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            adj[u].append(v)
        
        indegree = [0] * numCourses
        for i in range(numCourses):
            for it in adj[i]:
                indegree[it] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return count == numCourses