class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        self.helper(n, dp)
        return dp[-1]
    
    def helper(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        if n < 0:
            return 0
        if n == 1:
            dp[1] = 1
            return dp[1]
        if n == 2:
            dp[2] = 2
            return dp[2]
        
        dp[n] = self.helper(n-1,dp)+self.helper(n-2,dp)
        return dp[n]