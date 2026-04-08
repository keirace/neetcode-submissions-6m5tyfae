class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford

        # Track the best price to each node with up to k+1 stops
        cost = [float('inf')] * n
        cost[src] = 0 # [node][stops]

        # update any nodes reachable by the src node first, similar to bfs
        for i in range(k + 1):
            temp = cost.copy()
            for u, v, p in flights:
                # can't update dst if src is inf
                if cost[u] == float("inf"):
                    continue
                # update if cost + prev cost < cost[dst]
                if p + cost[u] < temp[v]:
                    temp[v] = p + cost[u]
            cost = temp

        return cost[dst] if cost[dst] != float('inf') else -1