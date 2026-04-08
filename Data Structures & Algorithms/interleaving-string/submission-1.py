class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        total = len(s3)
        if total != m + n:
            return False
        
        memo = {}
        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[i, j]
            if k == total:
                return i == m and j == n
            
            res = False
            if i < m and s3[k] == s1[i]:
                res = dfs(i+1, j, k+1)
            if not res and j < n and s3[k] == s2[j]:
                res = dfs(i, j+1, k+1)
            memo[i, j] = res
            return res
        
        return dfs(0,0,0)
