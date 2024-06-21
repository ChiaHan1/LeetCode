class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                profit.append(max(0, profit[-1]))
            else:
                profit.append(max(profit[-1], prices[i] - buy))
        return profit[-1]