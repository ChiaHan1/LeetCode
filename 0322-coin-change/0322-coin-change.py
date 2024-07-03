class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        
        # no coin needed for 0
        dp[0] = 0
        
        # for each coin
        for c in coins:
            # for each amount
            for x in range(c, amount + 1):
                # whether to use the coin or not
                dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1