class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        n = len(nums)
        minFound = inf
        while l <= r and r < n:
            target -= nums[r]
            while target <= 0:
                minFound = min(minFound, r-l+1)
                target+=nums[l]
                l+=1
            r+=1
        return 0 if minFound is inf else minFound
    
            
            
        