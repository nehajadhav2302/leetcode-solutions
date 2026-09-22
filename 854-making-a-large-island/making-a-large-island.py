class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if node == self.parent[node]:
            return node 
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)

        if ulp_u == ulp_v:
            return 
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def is_Valid(self, row, col, n):
        return 0 <= row < n and 0 <= col < n

    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        # Step 1: Connect adjacent 1s
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                for i in range(4):
                    nrow = row + dr[i]
                    ncol = col + dc[i]

                    if self.is_Valid(nrow, ncol, n) and grid[nrow][ncol] == 1:
                        node_no = row * n + col
                        adj_node = nrow * n + ncol
                        dsu.unionBySize(node_no, adj_node)
        
        max_count = 0

        # Step 2: Try converting each 0 to 1
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                
                components = set()

                for i in range(4):
                    nrow = row + dr[i]
                    ncol = col + dc[i]

                    if self.is_Valid(nrow, ncol, n) and grid[nrow][ncol] == 1:
                        node_no = nrow * n + ncol
                        components.add(dsu.find(node_no))
                
                size_total = 1
                for nodes in components:
                    size_total += dsu.size[nodes]
                
                max_count = max(max_count, size_total)

        for cell in range(n * n):
            max_count = max(max_count, dsu.size[dsu.find(cell)])

        return max_count