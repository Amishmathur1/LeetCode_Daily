from functools import cache
class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        # memo ={}
        @cache
        def cal(s:int)->int:
            # if s in memo:
            #     return memo[s]
            if s <=2:
                return s
        
            return cal(s-1)+cal(s-2)
            # return memo[s]
        return cal(n)

