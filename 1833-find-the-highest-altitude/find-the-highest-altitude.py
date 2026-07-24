class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_val = 0
        val = 0
        for i in gain:
            val += i 
            max_val = max(max_val, val)
        return max_val

