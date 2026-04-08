class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        
        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i]

        for i in range(n-1, 0, -1):
            postfix[i-1] = postfix[i]*nums[i]
        
        for i in range(n):
            postfix[i] = postfix[i] * prefix[i]

        return postfix
        

        '''
        pre     1  1  4 8
        post    48 24 6 1
        res     48 24 8 8
        '''