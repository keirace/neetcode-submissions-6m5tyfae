class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: return res
        digit_ch = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def dfs(i, sol):
            if i == len(digits):
                res.append(''.join(sol[:]))
                return
            
            for ch in digit_ch[int(digits[i])]:
                sol.append(ch)
                dfs(i+1, sol)
                sol.pop()
        dfs(0, [])
        return res