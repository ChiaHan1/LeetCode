class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # get the dimension of the grid
        m, n = len(grid), len(grid[0])
        
        # initialize a 2d array with 0s
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # base case - the starting point
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                # if (i, j) is not at the top row or leftmost column
                elif i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                # if (i, j) is at the leftmost column
                elif i - 1 >= 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                # if (i, j) is at the top row
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                    
        return dp[m - 1][n - 1]