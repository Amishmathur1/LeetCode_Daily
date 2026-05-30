class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        max_count = 0

        for i in range(len(nums)):

            print(l, r, count)

            if nums[r] == 1:
                count += 1
                r += 1

            else:
                count = 0
                l = r
                r += 1

            max_count = max(max_count, count)

        return (max_count)