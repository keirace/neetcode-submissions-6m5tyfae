class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]
        for sell in prices:
            maxprofit = max(maxprofit, sell-buy)
            buy = min(buy, sell)
        return maxprofit