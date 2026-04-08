class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        maxsub = nums[0]
        maxending = nums[0]
        for i in range(1, len(nums)):
            maxending = max(maxending + nums[i], nums[i])
            maxsub = max(maxsub, maxending)
        return maxsub