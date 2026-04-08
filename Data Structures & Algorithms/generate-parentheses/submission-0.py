class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(sol, openn, close):
            if close > openn or openn > n:
                return
                
            if len(sol) == 2*n:
                res.append(''.join(sol[:]))
                return

            for i in '()':
                sol.append(i)
                if i == '(':
                    backtrack(sol, openn+1, close)
                else:
                    backtrack(sol, openn, close+1)
                sol.pop()
            
        res = []
        backtrack([], 0, 0)
        return res