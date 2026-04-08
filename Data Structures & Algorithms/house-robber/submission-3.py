class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # bottom-up dp: tabulation
        memo = {0:nums[0], 1:max(nums[0], nums[1])}
        for i in range(2, len(nums)):
            # max of ROB or SKIP
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])

        return memo[len(nums)-1]