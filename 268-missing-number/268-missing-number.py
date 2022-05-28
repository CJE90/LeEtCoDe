class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fullSum = 0
        actualSum = 0
        for i in range(len(nums)):
            fullSum += i+1
            actualSum += nums[i]
        return fullSum-actualSum
    
   
        