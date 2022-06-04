class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.answer = [0 for _ in range(len(nums))]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            self.answer[i] = temp
        return self.answer