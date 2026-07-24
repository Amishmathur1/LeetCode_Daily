class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a1 = nums[:n-1]
        a2 = nums[1:]

        def func(ind,arr):
            if ind >= len(arr):
                return 0
            if dp[ind] != -1:
                return dp[ind]
            dp[ind] = max(arr[ind] + func((ind + 2), arr), func((ind + 1), arr))
            return dp[ind]

        dp = [-1] * len(a1)
        ans1 = func(0, a1)
        dp = [-1] * len(a1)
        ans2 = func(0, a2)

        return (max(ans1, ans2))