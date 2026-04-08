class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n+1))
        self.parentCount = n

        # Disjoint Set Union
        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            return parent[node]

        def union(x, y):
            px = findParent(x)
            py = findParent(y)
            if px == py:
                return False
            self.parentCount -= 1
            parent[py] = px
            return True

        for u, v in edges:
            if not union(u, v):
                return False
        
        return self.parentCount == 1
