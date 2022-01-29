class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        smallestValidWindow = len(nums)+1
        
        for r in range(len(nums)):
            target -= nums[r]
            while target <= 0:
                smallestValidWindow = min(smallestValidWindow, r-l+1)
                target += nums[l]
                l+=1
                
        return 0 if smallestValidWindow > len(nums) else smallestValidWindow
        
        