from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [False] * len(isConnected)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True

                while q:
                    node  = q.popleft()

                    for j in range(len(isConnected)):
                        if not visited[j] and isConnected[node][j] == 1:
                            q.append(j)
                            visited[j] = True
                
                provinces += 1
        return provinces
                    

