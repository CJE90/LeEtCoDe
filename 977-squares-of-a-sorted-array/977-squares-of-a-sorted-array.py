class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return_arr = []
        left = 0
        right = len(nums)-1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                return_arr.append(nums[left]**2)
                left += 1
            else:
                return_arr.append(nums[right]**2)
                right -= 1
        return return_arr[::-1]
        