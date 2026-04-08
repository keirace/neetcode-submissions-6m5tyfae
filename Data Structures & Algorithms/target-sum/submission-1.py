class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, curr):
            if i == n:
                return curr == target

            if i > n:
                return 0
            
            res = 0
            # add or subtract
            res += dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
            return res

        return dfs(0, 0)