class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            
            result += self.search_pairs(nums, nums[i], i+1, target)
        return result
    def search_pairs(self, nums, first_val, left, target):
        result = 0
        right = len(nums)-1
        while left< right:
            _sum = first_val + nums[left] + nums[right]
            if _sum < target:
                result += right-left
                left += 1
                # while left < right and nums[left] == nums[left-1]:
                #     left += 1
            else:
                right -= 1
                # while left < right and nums[right] == nums[right+1]:
                #     right -= 1
        return result
    
#      i L
#     -2,0,0,2,2
#              R
    