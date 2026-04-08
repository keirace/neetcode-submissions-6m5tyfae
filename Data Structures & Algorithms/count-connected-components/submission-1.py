class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # Time = O(V+E)
        # Space = O(V+E)

        # initialize an adjacency list
        adjlist = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        
        visited = set()
        count = 0
        def dfs(v):
            for neighbor in adjlist[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        # loop and count the number of graph
        for v in range(n):
            if v not in visited:
                visited.add(v)
                dfs(v)
                count += 1
        
        return count
