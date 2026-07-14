class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        
        if len(nums1) % 2 == 0:
            middle = len(nums1)//2
            abg = (nums1[middle] + nums1[middle-1]) / 2
            return abg
        else:
            mid = len(nums1) // 2
            return nums1[mid]