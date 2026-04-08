class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        while k:
            k -= 1
            num = -heapq.heappop(maxheap)
            if k == 0:
                return num