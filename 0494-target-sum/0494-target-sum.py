class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sum of all the numbers (offset for the array)
        total_sum = sum(nums)
        
        # check if target is achievable [-total_sum, total_sum]
        if target < -total_sum or target > total_sum:
            return 0
        
        # dp[i][s] = number of ways to achieve s using the first i numbers
        # (shifted by total_sum for indices of negative values)
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]
        
        # base case
        dp[0][nums[0] + total_sum] = 1 # add the first number
        dp[0][-nums[0] + total_sum] += 1 # subtract the first number
        
        # for each number in the array
        for i in range(1, len(nums)):
            # for each possible sum
            for s in range(-total_sum, total_sum + 1):
                # if s is achievable using the first (i - 1) numbers
                if dp[i - 1][s + total_sum] > 0:
                    # add nums[i] to s
                    dp[i][s + nums[i] + total_sum] += dp[i - 1][s + total_sum]
                    # subtract nums[i] from s
                    dp[i][s - nums[i] + total_sum] += dp[i - 1][s + total_sum]
        
        # return the result
        return dp[len(nums) - 1][target + total_sum]
        
        