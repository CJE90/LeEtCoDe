class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = oneCount = twoCount = 0
        for n in nums:
            if n == 0:
                zeroCount +=1
            elif n == 1:
                oneCount += 1
            else:
                twoCount += 1
        for i in range(len(nums)):
            if zeroCount > 0:
                nums[i] = 0
                zeroCount -=1
            elif oneCount > 0:
                nums[i] = 1
                oneCount -= 1
            else:
                nums[i] = 2
                twoCount -=1
                
                
        