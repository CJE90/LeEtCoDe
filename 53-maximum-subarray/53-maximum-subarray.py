class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = runSum = nums[0]
        for i in range(1,len(nums)):
            runSum = max(nums[i], runSum+nums[i])
            maxSum = max(runSum, maxSum)
        return maxSum