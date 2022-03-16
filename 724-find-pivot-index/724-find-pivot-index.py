class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1,8,11,17,23,29]
        # [28,27,20,17,11,6]
        
        leftToRight = [0 for i in range(len(nums))]
        rightToLeft = [0 for i in range(len(nums))]
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            leftToRight[i] = runSum
        runSum = 0
        for i in range(len(nums)-1,-1,-1):
            
            runSum += nums[i]
            rightToLeft[i] = runSum

       
            
        for i in range(len(nums)):
            if leftToRight[i] == rightToLeft[i]:
                return i
        return -1