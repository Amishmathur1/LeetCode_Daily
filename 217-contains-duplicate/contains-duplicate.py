from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) == len(nums):
        #     return False
        # else:
        #   
        

        # d = {}
        # for i in nums:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] += 1
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        # print(d)

        for i in d.values():
            if i > 1:
                return True
        return False