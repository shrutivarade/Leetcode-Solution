class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy everyday and sell immediately at higher price

        profit = 0
        buy = prices[0]
        n = len(prices)
        for sell in range(0 , n):
            if buy < prices[sell]: # check if we can sell when market open the next day.
                profit += prices[sell] - buy
            buy = prices[sell] # buy when market closes
        return profit

