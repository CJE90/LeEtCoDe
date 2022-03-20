class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        maxIndex = 0
        for i in range(1,len(nums)-k+1):
            if nums[maxIndex]< nums[i]:
                maxIndex = i
        return nums[maxIndex:maxIndex+k]