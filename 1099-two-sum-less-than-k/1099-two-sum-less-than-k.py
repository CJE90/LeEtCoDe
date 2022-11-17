class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        high_sum = -inf
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum < k:
                high_sum = max(high_sum, _sum)
                left += 1
            else:
                right -= 1
        return high_sum if high_sum != -inf else -1
        