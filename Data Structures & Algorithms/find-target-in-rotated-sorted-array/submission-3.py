class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        # Find cut.
        first, last = nums[0], nums[len(nums) - 1]
        # No cut.
        if first <= last:
            return self.binary_search(nums, target)
        # Find cut.
        index = len(nums) // 2
        size = len(nums) // 2
        cut_index = -1

        # Debugging...
        print(nums)
        print([i for i in range(len(nums))])

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                cut_index = mid + 1
                break

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        # Could not find cut index
        if cut_index < 0:
            return -1
        arr_higher, arr_lower = nums[:cut_index], nums[cut_index:]

        candidate_one = self.binary_search(arr_higher, target)
        if candidate_one >= 0:
            return candidate_one

        candidate_two = self.binary_search(arr_lower, target)
        print("Candidates", candidate_one, candidate_two)
        if candidate_two >= 0:
            return candidate_two + len(arr_higher)
        else:
            print("Could not find target even after cutting")
            return -1
             


        # Binary search
        # Problem: The first element I choose, I don't know
        # if it's the middle point.
        # I do know elements are sorted though, so I should know which
        # direction to shift.
        # We could shift by half. If resulting index < 0 or > len(nums), 
        # wrap around.
        # Then check! If somehow the value is larger, then we've gone too far.
        
        # Binary search to find "cut".
        # We can peek at the first and last element. If first<last, no cut.
        # Else, there is a cut and we must find it. 
        # Choose middle element. Check that it is > first. If so, 
        # the "cut" is to the right. If not, cut is to the left. 
        # Binary search from there. 

        # After the cut, we split into two arrays, keeping track of index
        # (2nd array indices is just len(1st_array) + i_of_second)
        # Binary search on both.

        # Runtime: Finding cut is O(log n), binary search twice is O(2log n)
        # Total is just O(log n)