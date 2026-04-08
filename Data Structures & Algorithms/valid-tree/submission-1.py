class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # get all the adj lists
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # BFS
        visited = set()
        visited.add(0)
        que = deque([(0, -1)])
        while que:
            node, parent = que.popleft()
            for successor in graph[node]:
                if successor == parent:
                    continue
                if successor in visited:
                    return False
                visited.add(successor)
                que.append((successor, node))
        
        return len(visited) == n