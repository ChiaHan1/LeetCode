class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # length of the first word
        n = len(word1)
        # length of the second word
        m = len(word2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # initialize for 1 from 1 to n, dp[i, 0] = i
        for i in range(1, n + 1):
            dp[i][0] = i
        # initialize for j from 1 to m, dp[0, j] = j
        for j in range(1, m + 1):
            dp[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j -1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j -1], 1 + dp[i - 1][j - 1])
        
        return dp[n][m]
            
        
        