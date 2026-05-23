class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        max_dif = nums[1] - nums[0]
        new_dif = nums[1] - nums[0]

        for i in range(1, len(nums)-1):
            new_dif = abs(nums[i+1] - (new_dif + nums[i-1]))
            max_dif = max(max_dif, new_dif)
        return max_dif