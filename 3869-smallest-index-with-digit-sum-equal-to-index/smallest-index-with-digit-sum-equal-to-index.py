class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for ind, val in enumerate(nums):
            x = str(val)
            l = sum([int(i) for i in x])
            if l == ind:
                return ind
        
        return -1