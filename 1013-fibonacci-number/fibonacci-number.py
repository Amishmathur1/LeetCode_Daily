class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)

        def fi(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = fi(n-1)+fi(n-2)
            return dp[n]
        
        return fi(n)
