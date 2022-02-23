class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        # dp = [0] * (len(cost)+1)
        # dp[0] = 0
        # dp[1] = 0
        # for i in range(2,len(cost)+1):
        #     dp[i] = min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        # return dp[len(cost)]
        memo = {}
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 0
            if n not in memo:
                memo[n] = min(cost[n-1]+dp(n-1), cost[n-2]+dp(n-2))
            return memo[n]
        return dp(len(cost))
        
        