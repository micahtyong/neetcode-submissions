# ith day before a "warmer temperature appears on a future day"

# Naive:
# For each elem in array,
# - For each elem up to that point in arr, see if currTemp > prevTemp 
# - If so, take currPos - len(list). Set that to the result array.
# In any case, add the item to the dict
# Runtime: Double for loop, O(n^2). Space complexity is const O(1)

# Better solution: O(n) time, O(n) space
# Can we make lookups / updates O(1)? We redundantly check "res[j] == 0"
# Use a stack instead, pop off stack if temp is higher than top of stack
# Each item in the stack has index, so we can easily update res
# Issue: If we look at top of stack first, we risk missing elems. Need queue instead?

# stack: [(38, 1), (30, 2)]
# res: [1, 0, 1, 0, 0, 0, 0]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # append to push, pop() to pop, stack[-1] to peek
        res = [0 for i in range(len(temperatures))]
        for i, currTemp in enumerate(temperatures):
            # print(stack, res, (currTemp, i))
            while stack and currTemp > stack[-1][0]:
                prevIndex = stack[-1][1]
                res[prevIndex] = i - prevIndex
                stack.pop()

            stack.append((currTemp, i)) # this should go on top
        # print(res)
        return res

    def dailyTemperaturesNaive(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        for i, currTemp in enumerate(temperatures):
            for j, prevTemp in enumerate(temperatures[:i]):
                if currTemp > prevTemp and res[j] == 0:
                    res[j] = i - j
        
        # print(res)
        return res
            