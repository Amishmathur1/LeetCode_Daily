class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = set(nums1)
        y = set(nums2)
        l = []
        for i in y:
            if i in x:
                l.append(i)
        return l