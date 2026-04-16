class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjlist = [[] for _ in range(n)]
        for u, v, c in edges:
            adjlist[u].append((v, c))

        heap = [(src, 0)] # (src, cost)
        res = {i: float('inf') for i in list(range(n))}
        res[src] = 0
        while heap:
            node, cost = heapq.heappop(heap)
            if cost > res[node]:
                continue
            for nei, nei_cost in adjlist[node]:
                new_cost = cost + nei_cost
                if new_cost < res[nei]:
                    res[nei] = new_cost
                    heapq.heappush(heap, (nei, new_cost))

        # cleanup the unreachable vertices
        for v in res.keys():
            if res[v] == float('inf'):
                res[v] = -1

        return res