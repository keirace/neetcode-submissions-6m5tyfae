class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # idea: want max count of previous num > cur
        n = len(nums)
        dp = [-1]*n
        dp[n-1] = 1

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            dp[i] = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dfs(j))
            return dp[i]

        return max(dfs(i) for i in range(n))