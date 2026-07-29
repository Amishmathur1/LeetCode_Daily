class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm 

        curr = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):
            curr += nums[i]
            if curr < nums[i]:
                curr = nums[i]
            maxi = max(maxi, curr)                

        return (maxi)