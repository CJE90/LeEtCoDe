class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[1] = 1
        if n > 1:
            dp[2] = 2
        self.helper(n, dp)
        return dp[-1]
    
    def helper(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        if n < 0:
            return 0
        
        dp[n] = self.helper(n-1,dp)+self.helper(n-2,dp)
        return dp[n]
        
        
        
        
        
        
        
        
        
        
        
        
        
        # 1: 1
        # 2: 1+1, 2
        # 3: 1+1+1, 2+1
        # 4: 1+1+1+1, 2+1+1, 2+2
        # 5: 1+1+1+1+1+1, 2+1+1+1, 2+2+1