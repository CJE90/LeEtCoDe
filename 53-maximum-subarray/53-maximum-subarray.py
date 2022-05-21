class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runSum = nums[0]
        maxSum = runSum
        for i in range(1,len(nums)):
            runSum = max(nums[i], runSum + nums[i])
            maxSum = max(maxSum, runSum)
            
        return maxSum
                
            
        