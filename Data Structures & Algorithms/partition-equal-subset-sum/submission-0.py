class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 :
            return False

        target = total // 2
        memo = [[-1] * (target + 1) for _ in range(len(nums)+1)]
        def dfs(i, target):
            if memo[i][target] != -1:
                return memo[i][target]
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False

            # include or skip
            memo[i][target] = dfs(i+1, target - nums[i]) or dfs(i+1, target)
            return memo[i][target]

        return dfs(0, target)