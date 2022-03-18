class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = -inf
        l = 0
        runSum = 0
        for r in range(len(nums)):
            runSum += nums[r]
            if r >= k:
                runSum -= nums[l]
                l += 1
            if r >= k - 1:
                maxSum = max(runSum, maxSum)
        return maxSum / k
            
        