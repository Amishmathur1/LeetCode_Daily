class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        arr = [0]
        for i in range(len(gain)):
            maxi = maxi + gain[i]
            arr.append(maxi)
        return max(arr)

