class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, p, r = 0, 0, len(nums)-1
        
        while p <= r:
            if nums[p] == 0:
                nums[l], nums[p] = nums[p], nums[l]
                p +=1
                l+=1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p],nums[r] = nums[r],nums[p]
                r-=1
        
        