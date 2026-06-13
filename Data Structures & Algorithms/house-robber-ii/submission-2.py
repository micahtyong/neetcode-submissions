# Circular ring buffer.

# Brute-force: Generate all possible permutations, return the max.
# "Rob this one" OR "Rob the next one"

# [3, 4, 3]
# l: [([0], 2), ([1], 3)]



class Solution:
    def rob(self, nums: List[int]) -> int:
        # Same but with DP memoization. 
        if len(nums) <= 2: return max(nums) 

        def helper(nums: List[int]) -> int:
            dp = [0] * len(nums) # Always stores max you can rob up to index i
            dp[0] = nums[0] # Rob this house
            dp[1] = max(dp[0], nums[1]) # Rob this house or don't bother.
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2]) # Don't rob this house, or do.
            
            return dp[len(nums) - 1]
        
        return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))
            
            

    def rob_naive(self, nums: List[int]) -> int:
        # Exponential in n, brute force
        
        # Values are always non-negative, so always accumulate.
        l = []
        for i, num in enumerate(nums):
            # Add (start fresh or append)
            l.append(([i], i + 2))
            for indices, next_valid in l:
                if i == len(nums) - 1 and indices[0] == 0:
                    # Circular buffer case
                    continue
                if i >= next_valid:
                    l.append((indices + [i], i + 2))
            # Skip
        print(l, len(l))
        
        max_profit = 0
        for indices, _ in l:
            profit = sum([nums[i] for i in indices])
            max_profit = max(profit, max_profit)
        
        return max_profit