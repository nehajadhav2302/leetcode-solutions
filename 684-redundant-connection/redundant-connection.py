class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return False
            
            if rank[pu] < rank[pv]:
                parent[pu] = pv
            elif rank[pu] > rank[pv]:
                parent[pv] = pu
            else:
                parent[pv] = pu
                rank[pu] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]