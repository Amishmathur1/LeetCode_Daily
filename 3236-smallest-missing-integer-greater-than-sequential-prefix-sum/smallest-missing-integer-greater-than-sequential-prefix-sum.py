class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ind = 1
        cur_sum = nums[0]
        while True:
            if ind < len(nums) and nums[ind] == nums[ind - 1] + 1:
                cur_sum += nums[ind]
                ind += 1
            else:
                break
        
        # nums = set(nums)
        while True:
            if cur_sum in nums:
                cur_sum += 1
            else:
                return cur_sum 