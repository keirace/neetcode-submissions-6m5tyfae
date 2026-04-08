class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        for i in nums:
            heapq.heappush(self.minheap, i)
            if len(self.minheap) > k:
                heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]