class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(len(nums)):
            if i+1 not in seen:
                return i+1
        return len(nums)+1
        