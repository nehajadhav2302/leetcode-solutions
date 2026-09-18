class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        ds = DisjointSet(n)
        cntExtras = 0

        for u, v in connections:
            if ds.findUPar(u) == ds.findUPar(v):
                cntExtras += 1
            else:
                ds.unionBySize(u, v)
        
        cntC = 0
        for i in range(n):
            if ds.parent[i] == i:
                cntC += 1
        ans = cntC - 1
        if cntExtras >= ans:
            return ans
        return -1