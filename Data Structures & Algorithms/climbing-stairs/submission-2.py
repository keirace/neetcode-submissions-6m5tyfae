class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up dp (tabulation)
        memo = {n:1, n-1:1}
        for i in range(n-2, -1, -1):
            memo[i] = memo[i+1] + memo[i+2]
        return memo[0]