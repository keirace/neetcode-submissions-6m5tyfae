class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            # reached
            if i >= len(nums)-1:
                return True
            # cannot reach
            if nums[i] == 0:
                return False
            for n in range(1, nums[i]+1):
                memo[i+n] = dfs(i+n)
            return any(v==True for v in memo.values())

        return dfs(0)