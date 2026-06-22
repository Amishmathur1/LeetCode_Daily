class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sol, ans = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                ans.append(sol[:])
                return 
            
            #Pick 
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #dont pick
            backtrack(i+1)
        
        backtrack(0)
        return ans