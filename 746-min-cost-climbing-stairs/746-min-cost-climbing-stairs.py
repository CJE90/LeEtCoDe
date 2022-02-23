class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        return dp[len(cost)]
        # memo = {}
        # def step(n):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 0
        #     if n not in memo:
        #         memo[n] = cost[n]+min(cost[n]+step(n-2), step(n-1))
        #     return memo[n]
        # return step(len(cost)-1)
        
        