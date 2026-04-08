class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's - min heap
        # no starting and end points -> not dijkstra
        # connect all points
        # cost = abs(x0-x1) + abs(y0-y1)
        n = len(points)
        # build a graph
        adjlist = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adjlist[i].append((cost, j))
                adjlist[j].append((cost, i))
        
        minheap = [(0, 0)]
        visited = set()
        res = 0
        # get minimum cost
        while len(visited) < n:
            cost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neicost, nei in adjlist[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (neicost, nei))
        return res