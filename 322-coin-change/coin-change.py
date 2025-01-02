class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        # Recursion
        # def min_coins(amount, coins):
        #     if amount == 0:
        #         return 0
        #     else:
        #         ans = float('inf')
        #         for coin in coins:
        #             subproblem = amount-coin
        #             if subproblem < 0:
        #                 continue
        #             ans = min(ans, min_coins(subproblem, coins)+1)
        #     return ans
        # return min_coins(amount, coins) if min_coins(amount, coins) != float('inf') else -1

        
        
        # Memoization with hashmap:
        memo = {}
        def min_coins(amount, coins):

            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0
            
            ans = float('inf')
            for coin in coins:
                subproblem = amount-coin
                if subproblem < 0:
                    continue
                ans = min(ans, min_coins(subproblem, coins)+1)
            memo[amount] = ans
            return ans
        
        return min_coins(amount, coins) if min_coins(amount, coins) != float('inf') else -1

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # greedy method developed by me and onkar ;)
        # count = 0
        # coins.sort()
        # i = len(coins)-1
        # while amount!=0 and i>=0:
        #     if amount >= coins[i]:
        #         temp = amount - amount % coins[i]
        #         count += temp // coins[i]
        #         amount = amount - temp
        #     i-=1

        # if amount!=0 and i<=0:
        #     return -1
        # else:
        #     return count




        # DP Method with array:
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount+1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1+dp[a-c])
        # return dp[amount] if dp[amount] != amount + 1 else -1
