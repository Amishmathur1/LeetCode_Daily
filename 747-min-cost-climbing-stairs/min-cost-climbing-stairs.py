class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
        n = len(cost)
        dp = [-1] * (n+1)

        def dfs(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            one = dfs(i+1)
            two = dfs(i+2)
            dp[i] = cost[i] + min(one, two)
            return cost[i] + min(one, two)
        
        return min(dfs(0), dfs(1))
        