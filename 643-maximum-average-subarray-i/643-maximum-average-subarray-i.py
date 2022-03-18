class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        maxSum = -inf
        l = 0
        runSum = 0
        for r in range(len(nums)):
            runSum += nums[r]
            if r - l + 1 > k:
                runSum -= nums[l]
                l += 1
            if r - l + 1 == k:  
                maxSum = max(maxSum, runSum)
        return maxSum / k
            
        