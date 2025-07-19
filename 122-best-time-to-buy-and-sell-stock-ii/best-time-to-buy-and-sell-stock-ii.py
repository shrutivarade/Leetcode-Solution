class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy everyday and sell immediately at higher price

        profit = 0
        buy = prices[0]
        n = len(prices)
        for sell in range(0 , n):
            if buy < prices[sell]: 
                profit += prices[sell] - buy
            buy = prices[sell]
        return profit

