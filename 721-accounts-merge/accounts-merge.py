class DSU:
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
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = DSU(n)

        mapMailNode = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]

                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    dsu.unionBySize(i, mapMailNode[mail])
        
        mergedMail = [[] for _ in range(n)]
        for mail, idx in mapMailNode.items():
            node = dsu.findUPar(idx)
            mergedMail[node].append(mail)
        
        ans = []
        for i in range(n):
            if not mergedMail[i]:
                continue
            mergedMail[i].sort()
            temp = [accounts[i][0]]
            temp.extend(mergedMail[i])
            ans.append(temp)
        ans.sort()
        return ans