class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == (tot - nums[i] - left):
                return i
        
            left += nums[i]    
        return -1