class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def tab(arr):
            dp = [0] * (len(arr) + 2)
            for i in range(len(arr)-1, -1, -1):
                dp[i] = max(arr[i] + dp[i+2], dp[i+1])
            return dp[0]
        ans1 = tab(nums[:n-1])
        ans2 = tab(nums[1:])    
        return (max(ans1, ans2))
