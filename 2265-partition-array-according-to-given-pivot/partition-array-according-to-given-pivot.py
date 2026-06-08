class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        h = []
        mid = []
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i > pivot:
                h.append(i)
            else:
                mid.append(i)
        return (l+mid+h)