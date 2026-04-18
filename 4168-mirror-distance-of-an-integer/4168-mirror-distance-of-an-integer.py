class Solution:
    def mirrorDistance(self, n: int) -> int:
        #Amish
        n = str(n)
        return abs(int(n) - int((n[::-1])))