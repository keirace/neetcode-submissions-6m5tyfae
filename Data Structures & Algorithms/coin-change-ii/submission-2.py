class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        coins.sort()

        for i in range(n-1, -1, -1):
            next_dp = [0] * (amount + 1)
            next_dp[0] = 1
            for a in range(amount+1):
                # next_dp[a] = dp[a]
                if a < coins[i]:
                    continue
                # take and no take
                next_dp[a] += next_dp[a-coins[i]] + dp[a]
            dp = next_dp

        return dp[amount]