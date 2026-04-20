class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic queue
        que = deque() # indices
        res = []
        for r, num in enumerate(nums):
            # descending order
            while que and num >= nums[que[-1]]:
                que.pop()
            
            que.append(r)

            # window size out of bounds:
            if r - que[0] >= k:
                que.popleft()
            
            # fulfilled the window size
            if r + 1 >= k:
                # greatest number at index 0
                res.append(nums[que[0]])
        
        return res
            
