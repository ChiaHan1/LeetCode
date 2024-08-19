class Solution:
    def minSteps(self, n: int) -> int:
        dp = [n] * (n + 1)
        # base case
        dp[1] = 0
        
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                # copy all and paste (i - j) / j times
                # for all valid j's
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        
        return dp[n]