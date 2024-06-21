class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 1):
            return 1
        steps = {}
        steps[0] = 1
        steps[1] = 1
        for i in range(2, n):
            steps[i] = (steps[i - 1] + steps[i - 2])
        return steps[n - 1] + steps[n - 2]