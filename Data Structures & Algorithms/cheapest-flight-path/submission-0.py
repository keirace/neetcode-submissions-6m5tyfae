class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijskstra

        # build an adjacency list
        adjlist = [[] for _ in range(n)]
        for u, v, price in flights:
            adjlist[u].append((price, v))
        
        # start from 0, src
        minheap = [(0, src, 0)]  # cost, node, stops

        # Track the best price to each node with up to k+1 stops
        cost = [[float('inf')] * (k + 2) for _ in range(n)]
        cost[src][0] = 0 # [node][stops]

        while minheap:
            curr_cost, node, stops = heapq.heappop(minheap)
            if node == dst:
                return curr_cost
            if stops > k:
                continue
            for price, nei in adjlist[node]:
                # check if new price is cheaper
                nextStops = 1 + stops
                next_cost = curr_cost + price
                if next_cost < cost[nei][nextStops]:
                    # update price
                    cost[nei][nextStops] = next_cost
                    heapq.heappush(minheap, (cost[nei][nextStops], nei, nextStops))
    
        return -1