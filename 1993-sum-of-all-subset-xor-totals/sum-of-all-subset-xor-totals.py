class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def dfs(ind, path):
            nonlocal ans
            if ind >= len(nums):
                temp = 0
                for i in path:
                    temp = temp ^ i
                ans += temp
                return 
            
            #Pick 
            path.append(nums[ind])
            dfs(ind + 1, path)

            #Not-Pick
            path.pop()
            dfs(ind + 1, path)
        
        dfs(0, [])
        return ans