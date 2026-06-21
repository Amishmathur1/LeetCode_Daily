class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        l = 0
        count = 0
        
        for l in range(len(nums)):
            curr_sum = 0

            for r in range(l, len(nums)):
                curr_sum += nums[r]

                s = str(curr_sum)

                if s[0] == str(x) and s[-1] == str(x):
                    count += 1

        return (count)
