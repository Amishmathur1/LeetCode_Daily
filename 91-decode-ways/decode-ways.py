class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        def dfs(ind):
            if ind >= len(s):
                return 1
            if s[ind] == '0':
                return 0
            if dp[ind] != -1:
                return dp[ind]
            ans = dfs(ind + 1)
            if ind < len(s) and 10 <= int(s[ind: ind+2]) <= 26:
                ans += dfs(ind + 2)
            dp[ind] = ans
            return dp[ind]
        return dfs(0)