class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm 

        curr_sum = 0
        max_sum = -1000000

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum < 0:
                max_sum = max(curr_sum, max_sum)
                curr_sum = 0
            else:
                max_sum = max(curr_sum, max_sum)
        return max_sum