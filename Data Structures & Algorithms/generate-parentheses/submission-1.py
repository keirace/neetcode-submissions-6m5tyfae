class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(sol, openn, close):
            if close == openn == n:
                res.append(''.join(sol))
                return

            if openn < n:
                sol.append('(')
                backtrack(sol, openn+1, close)
                sol.pop()
            if close < openn:
                sol.append(')')
                backtrack(sol, openn, close+1)
                sol.pop()
            
        res = []
        backtrack([], 0, 0)
        return res