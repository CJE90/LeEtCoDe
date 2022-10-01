class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = math.inf
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - _sum)
                if _sum == target:
                    return target
                if diff < abs(result - target):
                    result = _sum
                if _sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                else:
                    right -= 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
        return result
    
#          i  l    
#         -4,-1,1,2
#                 r  
            
#             _sum = -3
#             diff = 4
        