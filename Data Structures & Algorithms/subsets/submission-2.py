class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, sol):
            res.append(sol[:])

            for j in range(i, len(nums)):
                sol.append(nums[j])
                backtrack(j+1, sol)
                sol.pop()

        res = []
        backtrack(0, [])
        return res