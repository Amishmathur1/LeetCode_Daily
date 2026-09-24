class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for ind, val in enumerate(nums):
            if sum([int(i) for i in str(val)]) == ind:
                return ind
        return -1