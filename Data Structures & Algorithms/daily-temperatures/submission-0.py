# ith day before a "warmer temperature appears on a future day"

# Naive:
# For each elem in array,
# - For each elem up to that point in arr, see if currTemp > prevTemp 
# - If so, take currPos - len(list). Set that to the result array.
# In any case, add the item to the dict
# Runtime: Double for loop, O(n^2). Space complexity is const O(1)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        for i, currTemp in enumerate(temperatures):
            for j, prevTemp in enumerate(temperatures[:i]):
                if currTemp > prevTemp and res[j] == 0:
                    res[j] = i - j
        
        # print(res)
        return res
            