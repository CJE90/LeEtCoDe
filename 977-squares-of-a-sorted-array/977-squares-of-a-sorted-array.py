class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            nums[0] *= nums[0]
            return nums
        result = []
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l]*nums[l] >= nums[r]*nums[r]:
                result.append(nums[l]*nums[l])
                l+=1
            else:
                result.append(nums[r]*nums[r])
                r-=1
        return result[::-1]
                
        