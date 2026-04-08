class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i] * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= postfix
            postfix *= nums[i]
        return prefix