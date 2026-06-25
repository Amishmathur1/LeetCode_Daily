class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        visited = set()

        def dfs(ind, arr):
            if ind >= len(nums) and tuple(arr) not in visited:
                ans.append(arr[:])
                visited.add(tuple(arr))
                return 
            elif tuple(arr) in visited:
                return 
            
            #pick 
            arr.append(nums[ind])
            dfs(ind+1, arr)

            #not pick
            arr.pop()
            dfs(ind+1, arr)
        dfs(0, [])
        return ans