class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        k = []
        for i in nums:
            for j in str(i):
                k.append(int(j))
        return k