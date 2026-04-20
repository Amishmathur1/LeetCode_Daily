class Solution:
    def maxDistance(self, l: List[int]) -> int:
        max = 0
        for i in range(len(l)-1):
            for j in range(i, len(l)):
                if l[i] != l[j]:
                    max = abs(i - j) if max < abs(i - j) else max
        return max