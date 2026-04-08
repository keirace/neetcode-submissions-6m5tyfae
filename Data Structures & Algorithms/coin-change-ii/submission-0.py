class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def dfs(i, a):
            if (i, a) in memo:
                return memo[i, a]
            if a == 0:
                return 1
            if a < 0 or i == len(coins):
                return 0
            
            # Choose coin[i] (stay at i) or skip coin[i] (move to i+1)
            memo[i, a] = dfs(i, a-coins[i]) + dfs(i+1, a)
            return memo[i, a]

        coins.sort()
        return dfs(0, amount)