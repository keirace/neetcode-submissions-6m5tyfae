class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxheap = [-count for count in counter.values()]
        heapq.heapify(maxheap)

        time = 0
        que = deque() # pairs of [-cnt, idleTime]
        while maxheap or que:
            time += 1
            if not maxheap: # no tasks available
                time = que[0][1]
            else: # tasks available
                count = heapq.heappop(maxheap) + 1
                if count: # still has remaining count
                    que.append([count, time + n])
            if que and que[0][1] == time: # cooldown finished
                heapq.heappush(maxheap, que.popleft()[0])
        return time