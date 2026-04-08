class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            # most significant bit at that pos
            if i == offset*2: # from 2 onwards
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp