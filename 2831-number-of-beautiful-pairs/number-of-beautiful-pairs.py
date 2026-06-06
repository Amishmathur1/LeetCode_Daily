from math import gcd

class Solution:
    def countBeautifulPairs(self, nums):
        count = 0

        for i in range(len(nums)):
            first = int(str(nums[i])[0])

            for j in range(i + 1, len(nums)):
                last = nums[j] % 10

                if gcd(first, last) == 1:
                    count += 1

        return count