class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, cursum):
            if cursum == target:
                res.append(sol[:])
                return
            if cursum > target or i == len(candidates):
                return

            # include
            sol.append(candidates[i])
            backtrack(i+1, cursum + candidates[i])
            sol.pop()

            # skip: must include before checking if duplicates
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, cursum)

        candidates.sort()
        res, sol = [],[]
        backtrack(0, 0)
        return res