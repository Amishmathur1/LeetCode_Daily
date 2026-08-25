class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        number = k
        while True:
            if number not in nums:
                return number
            
            number += k
        