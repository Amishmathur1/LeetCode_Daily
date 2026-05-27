class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        x = 0
        while x < len(nums):    
            k = []
            for i in range(len(nums)):
                if i == x:
                    continue
                else:
                    k.append(nums[i])
            x += 1
            if all(k[i] < k[i+1] for i in range(len(k)-1)):
                return True
        return False