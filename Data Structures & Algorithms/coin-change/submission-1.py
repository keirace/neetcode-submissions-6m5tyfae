class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up dp
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == 0:
                return 0
            res = float('inf')
            for c in coins:
                if i - c >= 0:
                    res = min(dfs(i-c)+1, res)
            cache[i] = res
            return cache[i]
        mincoins = dfs(amount)
        return mincoins if mincoins < float('inf') else -1
