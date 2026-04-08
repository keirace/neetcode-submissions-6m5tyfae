class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        # Using DFS:
        # 1. Initialization: Start with an unvisited graph and mark all nodes as unvisited.
        visited = set()
        adjlist = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        print(adjlist)

        # 2. Traversal: Perform a DFS traversal, keeping track of the parent of each visited node.
        def dfs(v, pre):
            # 3. Cycle Detection: If, during the traversal, you encounter a neighbor that has been visited and is not the parent of the current node, then a cycle exists. This is because the neighbor was reached through a different path, indicating a back edge.
            if v in visited:
                return False

            visited.add(v)
            for adj in adjlist[v]:
                if adj == pre:
                    continue
                if not dfs(adj, v):
                    return False
            return True

        # 4. Complete Traversal: If the DFS completes without finding any such back edges, the graph is acyclic. 
        return dfs(0, -1) and len(visited) == n