class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        l = [0]
        for i in gain:
            height += i
            l.append(height)
        return max(l)