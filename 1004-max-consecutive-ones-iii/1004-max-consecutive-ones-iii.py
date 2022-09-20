class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_window = 0
        ones_count = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                ones_count += 1
            if right-left+1 - ones_count > k:
                if nums[left] == 1:
                    ones_count -= 1
                left += 1
            max_window = max(max_window, right-left +1)
        return max_window
        