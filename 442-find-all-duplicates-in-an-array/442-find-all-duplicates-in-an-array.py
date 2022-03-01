class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for val in nums:
            curVal = abs(val)-1
            nums[curVal] *= -1
        for val in nums:
            curVal = abs(val)-1
            if nums[curVal] > 0:
                result.append(abs(val))
                nums[curVal] *= -1
        return result