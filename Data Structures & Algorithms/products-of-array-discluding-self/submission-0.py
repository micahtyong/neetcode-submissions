# Naive: O(n^2) if you recompute each time
# (n - 1) + (n - 1) ... // n times for each element
# Better: n - 1 + n => O(n) if you shift / divide / multiply
#   - But how would you handle the division by 0 case?
# Follow-up

# Prefix-sum? Prefix-mult? 
# [1, 2, 8, 48]

# Left to right AND right to left
# [1, 2, 4, 6]
#   => 1, 1, 2, 8
#   => 48, 24, 6, 1
# Then multiply

# [-1, 0, 1, 2, 3]
#   => 1, -1, 0, 0, 0
#   => 0, 6, 6, 3, 1

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_reversed = nums[::-1]
        l2r, r2l = [1], [1]
        # Populate l2r
        for i in range(0, len(nums) - 1):
            l2r.append(l2r[-1] * nums[i])
            r2l.insert(0, r2l[0] * nums_reversed[i])
        
        print(l2r, r2l)
        res = []
        for i in range(len(nums)):
            res.append(l2r[i] * r2l[i])
        print(res)
        return res


