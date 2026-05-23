class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        d = dict(d)
        x = max(d.values())
        for i, j in d.items():
            if j == x:
                return i