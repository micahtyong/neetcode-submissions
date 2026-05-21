# Naive: Double-for loop, two pointers O(n^2)
# Better: O(n) time using two pointers, only moving in one direction
# Minimize start, maximize end where start < end
# Walk two pointers down towards each other
# You need to know when to walk it. 
# [10, 10, 1000, 10, 0, 100]
# Maybe too complicated to walk it in certain direction.

# Better pt 2: Two pointers next two each other
# Track min and max

# min is left of i. prices[i] - min is profit. maximize profit

import math 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
          if prices[i] < buy: # buy
            buy = prices[i]
          else: # sell
            profit = max(prices[i] - buy, profit) 
        return profit
            

                

    def maxProfitNaive(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit