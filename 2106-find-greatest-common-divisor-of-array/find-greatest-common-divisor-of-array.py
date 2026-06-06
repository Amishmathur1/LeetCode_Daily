class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        big = max(nums)

        # Finding GCD
        res = min(small, big)
        while res > 1:
            if small%res == 0 and big%res == 0:
                break
            res -= 1
        
        return res