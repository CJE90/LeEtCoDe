class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(n):
            if n == 0:
                return nums[0]
            if n == 1:
                
                return max(nums[0],nums[1])
            if n not in memo:
                memo[n] = max(dfs(n-1), nums[n]+dfs(n-2))
            
            return memo[n]
        
        return dfs(len(nums)-1)
        