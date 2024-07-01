class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # the dimension of the grid (m x n)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0]:
            return 0
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                # ignore the obstacle
                if obstacleGrid[i][j]:
                    continue
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i - 1 >= 0:
                    dp[i][j] = dp[i - 1][j]
                elif j - 1 >= 0:
                    dp[i][j] = dp[i][j - 1]
        return dp[m - 1][n - 1]
                