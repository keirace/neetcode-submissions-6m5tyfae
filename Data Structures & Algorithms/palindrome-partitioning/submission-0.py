class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i):
            if i == len(s):
                res.append(sol[:])
                return
            
            for j in range(i, len(s)):
                new_s = s[i:j+1]
                if new_s == new_s[::-1]:
                    sol.append(new_s)
                    dfs(j+1)
                    sol.pop()
        res, sol = [], []
        dfs(0)
        return res