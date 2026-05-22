class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case.
        if len(nums) == 0 or nums == []:
            return [[]]

        first_elem = nums[0]
        # Recursive cases.
        with_first = [[first_elem] + l for l in self.subsets(nums[1:])]
        without_first = self.subsets(nums[1::])

        return with_first + without_first