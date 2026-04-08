class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, sol):
            if i >= len(nums):
                if sol not in res:
                    res.append(sol[:])
                return

            # skip
            backtrack(i+1, sol)

            # choose
            sol.append(nums[i])
            backtrack(i+1, sol)
            sol.pop()

        res = []
        backtrack(0, [])
        return res