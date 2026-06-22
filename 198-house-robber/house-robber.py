from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        @cache
        def func(ind, curr_sum):
            if ind > n-1:
                return curr_sum
            
            pick = func(ind + 2, curr_sum + nums[ind])
            not_pick = func(ind + 1, curr_sum)
            return max(pick, not_pick)
        
        return func(0,0) 
        