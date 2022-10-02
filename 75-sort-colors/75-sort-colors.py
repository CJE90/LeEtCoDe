class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(nums)-1
        i = 0
        while i <= hi:
            if nums[i] == 0:
                nums[lo],nums[i] = nums[i],nums[lo]
                i += 1
                lo += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[hi],nums[i] = nums[i],nums[hi]
                hi-=1
        