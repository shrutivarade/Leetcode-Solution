class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        for i in range(0, len(prices)):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j]<= prices[i]:
                    discount = prices[j]
                    break
                
            prices[i] -= discount
        
        return prices
        