class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        for i in range(len(nums)):
            right = nums[:i+1]
            left = nums[i:]
            print(right, left)

            if max(right) - min(left) <= k:
                return (i)
        
        return -1