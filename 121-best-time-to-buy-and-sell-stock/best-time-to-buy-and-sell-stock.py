class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force : O(n^2)
        # profit = 0
        # for buy in range(0,len(prices)):
        #     for sell in range(buy+1, len(prices)):
        #         if(prices[sell]>prices[buy]):
        #             profit = max(prices[sell] - prices[buy], profit)
        # return profit

        # Optimal: O(n)
        profit = 0 
        buy = prices[0]

        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit,sell-buy)
            else:
                buy = sell

        return profit