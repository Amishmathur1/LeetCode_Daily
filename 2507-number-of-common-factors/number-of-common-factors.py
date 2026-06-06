class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0

        res = min(a,b)
        while res > 0:
            if a%res == 0 and b%res == 0:
                count += 1
            res -= 1
        return count