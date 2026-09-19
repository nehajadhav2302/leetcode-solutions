class DSU:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        dsu = DSU()
        for x, y in stones:
            dsu.union(x, y + 10001)
        
        components = set()

        for x, y in stones:
            components.add(dsu.find(x))
        
        return len(stones) - len(components)