class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            new = abs(x-y)
            if new > 0:
                heapq.heappush(heap, -new)
        return -heap[0] if heap else 0