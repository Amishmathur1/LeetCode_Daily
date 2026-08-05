class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        mini = min(nums)
        ans = []
        for i in range(mini, maxi+1):
            if i not in nums:
                ans.append(i)
        
        return ans
