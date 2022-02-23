class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[len(nums)-1]
        
        
#         memo = {}
#         def dfs(n):
#             if n == 0:
#                 return nums[0]
#             if n == 1:
                
#                 return max(nums[0],nums[1])
#             if n not in memo:
#                 memo[n] = max(dfs(n-1), nums[n]+dfs(n-2))
            
#             return memo[n]
        
#         return dfs(len(nums)-1)
        