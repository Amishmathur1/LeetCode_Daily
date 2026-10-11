class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumi = 0
        for i in range(len(nums)):
            if len(nums)%(i+1) == 0:
                sumi += nums[i]**2
        
        return sumi