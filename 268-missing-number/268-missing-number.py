class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingValSum = sum(nums)
        for i in range(len(nums)+1):
            missingValSum -= i
        return abs(missingValSum)
            
        