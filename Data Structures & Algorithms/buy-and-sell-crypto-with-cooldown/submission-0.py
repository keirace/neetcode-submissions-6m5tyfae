class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buy):
            if (i, buy) in memo:
                return memo[i, buy]
            if i >= len(prices):
                return 0

            # cooldown
            cooldown = dfs(i+1, buy)
            # buy
            if buy:
                memo[(i, buy)] = max(dfs(i+1, not buy) - prices[i], cooldown)

            # sell
            else:
                memo[(i, buy)] = max(dfs(i+2, not buy) + prices[i], cooldown)
            return memo[i, buy]

        return dfs(0, True)