class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minWindow = len(nums)+1
        for r in range(len(nums)):
            target -= nums[r]
            while target <= 0:
                minWindow = min(minWindow, r-l+1)
                target += nums[l]
                l+=1
        return minWindow if minWindow < len(nums)+1 else 0