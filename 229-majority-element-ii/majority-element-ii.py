class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        x = len(nums) // 3

        k = []

        for i, j in d.items():
            if j > x:
                k.append(i)
        return k