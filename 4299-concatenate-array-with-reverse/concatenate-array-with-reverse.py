class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev = nums[:]
        def reverse(l, r):
            if l>=r:
                return 
            
            rev[l], rev[r] = rev[r], rev[l]
            reverse(l+1, r-1)
        reverse(0, len(nums)-1)

        return nums+rev
