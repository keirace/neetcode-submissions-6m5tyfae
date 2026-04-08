class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time: O((V + E) log V)
        # Step 1: Build graph
        edges = defaultdict(list)
        for src, dest, time in times:
            edges[src].append((time, dest))
        
        # Step 2: Dijkstra’s algorithm from node k
        minheap = [(0, k)]
        delay_time = [float('inf') for _ in range(n+1)]
        delay_time[k] = 0
        while minheap:
            curr_time, node = heapq.heappop(minheap)
            if curr_time > delay_time[node]: # else get shorter path
                continue
            for new_time, neighbor in edges[node]:
                if delay_time[neighbor] > curr_time+new_time:
                    delay_time[neighbor] = curr_time+new_time
                    heapq.heappush(minheap, (delay_time[neighbor], neighbor))

        max_delay = max(delay_time[1:])
        return max_delay if max_delay != float('inf') else -1                

