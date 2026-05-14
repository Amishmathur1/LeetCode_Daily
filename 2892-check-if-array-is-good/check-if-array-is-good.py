class Solution:
    def isGood(self, nums: List[int]) -> bool:
       n = max(nums)
       l = [i for i in range(1,n+1)]
       l.append(n)
       nums.sort()
       if l == nums:
        return True
       else:
        return False
        