class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        runSum = sum(nums)
        leftSum = 0
        for index, num in enumerate(nums):
            if leftSum == (runSum - leftSum - num):
                return index
            leftSum += num
        return -1