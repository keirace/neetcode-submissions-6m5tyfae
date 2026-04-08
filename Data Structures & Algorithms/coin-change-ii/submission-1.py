class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[0] * (amount + 1) for _ in range(n+1)]

        for i in range(n+1):
            memo[i][0] = 1

        coins.sort()

        for i in range(n-1, -1, -1):
            for a in range(amount+1):
                if a < coins[i]:
                    continue
                # take and no take
                memo[i][a] = memo[i][a-coins[i]] + memo[i+1][a]

        return memo[0][amount]