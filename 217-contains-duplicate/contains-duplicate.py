class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) == len(nums):
        #     return False
        # else:
        #   
        freq = Counter(nums)
        for i in freq.values():
            if i > 1:
                return True
        return False