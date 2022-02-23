class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n<=2:
            return 1
        x,y,z = 0,1,1
        for _ in range(n-2):
            x,y,z = y,z,z+y+x
        return z
        # if n == 0:
        #     return 0
        # if n<= 2:
        #     return 1
        # dp = [0]*(n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        # for i in range(3,n+1):
        #     dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
        # return dp[n]
        
        
#         memo={}
        
#         def dp(n):
#             if n == 0:
#                 return 0
#             if n <= 2:
#                 return 1
#             if n not in memo:
#                 memo[n] = dp(n-3)+dp(n-2)+dp(n-1)
#             return memo[n]
#         return dp(n)

        
        
        
        
        