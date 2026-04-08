class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Top-down dp
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)