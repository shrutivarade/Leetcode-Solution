class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        # def ways(amount, coins, count):
        #     if amount == 0 :
        #         return 1
        #     for coin in coins:
        #         subproblem = amount-coin
        #         if subproblem<0:
        #             continue
        #         count += ways(subproblem, coins, count) if ways(subproblem, coins, count)==1 else 0
        #     return count
        # return ways(amount, coins, 0)


        # No of way to reach 5, choices 1,4,5

        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for amt in range(coin, amount+1):
                dp[amt] += dp[amt-coin]
        return dp[amount]