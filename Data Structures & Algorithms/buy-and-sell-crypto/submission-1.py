# Naive: Double-for loop, O(n^2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit