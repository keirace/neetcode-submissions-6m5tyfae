class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # which edge can be removed
        # idea: find a cycle, remove an edge in there
        # Time: O(V+E*α(V)) α() is used for amortized complexity
        # Space: O(V)
        n = len(edges)+1
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
                return False
            parent[py] = px
            numParents -= 1
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
        return []