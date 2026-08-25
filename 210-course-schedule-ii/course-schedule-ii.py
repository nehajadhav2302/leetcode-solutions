from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for neigh in adj[node]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return res if len(res) == numCourses else []