class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = 10000
        for i in nums:
            summ = 0
            x = str(i)
            for j in x:
                summ += int(j)
            min_sum = min(min_sum, summ)
        return min_sum