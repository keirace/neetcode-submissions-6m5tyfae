class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(j, sol):
            if sum(sol) == target:
                res.append(sol[:])
                return
            if sum(sol) > target:
                return
            
            for i in range(j, len(nums)):
                sol.append(nums[i])
                backtrack(i, sol)
                sol.pop()
        
        res = []
        backtrack(0, [])
        return res