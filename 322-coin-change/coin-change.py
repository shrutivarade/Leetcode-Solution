class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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

        # DP Method:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
