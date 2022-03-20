class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = 0
        maxSum = -inf
        l = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            if r >= k - 1:
                maxSum = max(maxSum, windowSum)
                windowSum -= nums[l]
                l+=1
        return maxSum / k
       
            
            
            
        