class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        count = 0
        ans = 0
        curSum = 0
        
        for r in range(len(nums)):
            curSum += nums[r]
            
            if nums[r] == 1:
                count = 0
                
            while l <= r and curSum >= goal:
                if curSum == goal:
                    count +=1
                curSum -= nums[l]
                l+=1
                
            ans += count
        return ans
            