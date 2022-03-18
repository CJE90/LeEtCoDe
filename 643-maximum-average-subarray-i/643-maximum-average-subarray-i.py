class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = cur = sum(nums[:k])
        print(maxsum)
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k] 
            if cur > maxsum: maxsum = cur
        return maxsum / k
            
            
            
        