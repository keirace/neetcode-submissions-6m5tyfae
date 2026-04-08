class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def recurse(nums):
            if not nums:
                return 0
            dp = [float('-inf')]*(len(nums)+1)
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(1, len(nums)):
                # if rob += nums[i] + profit at i-2
                # else: previous profit
                dp[i+1] = max(dp[i], nums[i]+dp[i-1])
            return dp[-1]

        # not include the last house, includes the last house
        return max(recurse(nums[1:]), recurse(nums[:-1]))