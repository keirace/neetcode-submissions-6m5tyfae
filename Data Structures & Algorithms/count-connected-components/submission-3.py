class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # disjoint set union
        parent = list(range(n))
        numParents = n

        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(x, y):
            nonlocal numParents
            px = findParent(x)
            py = findParent(y)
            if px == py:
                return
            parent[py] = px
            numParents -= 1
        
        for x, y in edges:
            union(x, y)
        
        return numParents