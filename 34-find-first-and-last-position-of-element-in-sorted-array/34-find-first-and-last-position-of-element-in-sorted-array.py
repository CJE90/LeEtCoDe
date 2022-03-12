class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def findBound(nums, target, isFirst):
            lo = 0
            hi = len(nums)-1
            while lo <= hi:
                mid = (lo+hi) // 2
                if nums[mid] == target:
                    if isFirst:
                        if mid == lo or nums[mid-1] != target:
                            return mid
                        else:
                            hi = mid-1
                    else:
                        if mid == hi or nums[mid+1] != target:
                            return mid
                        else:
                            lo = mid+1
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return -1
        
        result = []
        result.append(findBound(nums, target, True))
        result.append(findBound(nums, target, False))
        return result
            
            
        