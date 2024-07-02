class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # get the dimension of the grid
        m, n = len(grid), len(grid[0])
        
        # initialize an m x n array with 0s
        dp = [[0] * n for _ in range(m)]
        
        # base case - the starting point
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                # if (i, j) is not at the top row or leftmost column
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                # if (i, j) is at the leftmost column
                elif i - 1 >= 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                # if (i, j) is at the top row
                elif j - 1 >= 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                # skipping base case
                else:
                    continue
        return dp[m - 1][n - 1]