class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for index,value in enumerate(nums):
            index_to_change = abs(value)-1
            if nums[index_to_change] > 0:
                nums[index_to_change] *= -1
        for index,value in enumerate(nums):
            if value > 0:
                result.append(index+1)
        return result
    
    
    
    
#     [4  3  2  7  8  2  3  1]
#     [-4-3 -2 -7       -3  -1]
        