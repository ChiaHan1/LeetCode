class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # iterate through each house
        for i in range(1, len(costs)):
            # optimal cost up to this house based on color
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        
        return min(costs[-1])