class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # dont want to add duplicate subsets
        def backtrack(i):
            if i >= len(nums):
                res.append(sol[:])
                return

            # include
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            # skip
            backtrack(i+1)

        res, sol = [], []
        nums.sort()
        backtrack(0)
        return res