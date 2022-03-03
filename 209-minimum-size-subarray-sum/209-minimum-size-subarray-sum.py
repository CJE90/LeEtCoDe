class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLength = len(nums)+1
        
        for right in range(len(nums)):
            target -= nums[right]
            while target <= 0:
                minLength = min(minLength, right-left+1)
                target += nums[left]
                left+=1
        return 0 if minLength == len(nums)+1 else minLength
        