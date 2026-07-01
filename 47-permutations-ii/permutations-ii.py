class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []        
        nums.sort()        
        n = len(nums)
        x = [False] * n

        def dfs(path):
            nonlocal n
            if len(path) == n:
                ans.append(path[:])
                return 
            
            for i in range(n):
                if x[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not x[i-1]:
                    continue
                path.append(nums[i])
                x[i] = True
                dfs(path)
                path.pop()
                x[i] = False
            
        dfs([])
        return ans