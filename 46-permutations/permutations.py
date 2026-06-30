class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def func(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            
            for num in nums:
                if num in path:
                    continue
                
                path.append(num)
                func(path)
                path.pop()
        
        func([])
        return ans