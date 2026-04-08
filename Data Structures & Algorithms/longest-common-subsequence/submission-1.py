class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top-down dp
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            # match
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
                return dp[i][j]

            # not match, try other combos
            dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[i][j]
        return dfs(0, 0)