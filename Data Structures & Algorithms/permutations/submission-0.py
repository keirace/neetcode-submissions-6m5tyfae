class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in nums:
                if i in sol:
                    continue
                sol.append(i)
                backtrack(sol)
                sol.pop()
        res = []
        backtrack([])
        return res