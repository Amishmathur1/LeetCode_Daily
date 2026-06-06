class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        right_sum = []

        for i in range(len(nums)): 
            left_sum.append(sum(nums[:i]))

        for i in range(len(nums)):
            right_sum.append(sum(nums[i+1:]))

        ans = []
        x = 0
        for i in range(len(left_sum)):
            ans.append(abs(left_sum[i] - right_sum[i]))
        return (ans)