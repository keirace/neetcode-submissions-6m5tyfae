class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS
        # Time = O(V+E)
        # Space = O(V+E)

        # initialize an adjacency list
        adjlist = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        
        count = 0
        que = deque()
        visited = set()
        
        # loop and count the number of graph
        for v in range(n):
            if v not in visited:
                count += 1
                que.append(v)
                visited.add(v)
                while que:
                    node = que.popleft()
                    for neighbor in adjlist[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            que.append(neighbor)
        
        return count
