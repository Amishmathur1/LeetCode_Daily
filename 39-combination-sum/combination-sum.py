class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(ind, arr):
            if sum(arr[:]) == target:
                ans.append(arr[:])
                return 
            
            if sum(arr[:]) > target:
                return
            
            if ind >= len(nums):
                return 
            
            #pick
            arr.append(nums[ind])
            dfs(ind, arr)

            #not pick 
            arr.pop()
            dfs(ind+1, arr)
        
        dfs(0, [])
        return ans