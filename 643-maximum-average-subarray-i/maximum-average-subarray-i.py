class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind_sum = sum(nums[:k])
        max_sum = wind_sum

        for i in range(k, len(nums)):
            wind_sum -= nums[i-k]
            wind_sum += nums[i]
            max_sum = max(wind_sum, max_sum)

        return (max_sum/k)
