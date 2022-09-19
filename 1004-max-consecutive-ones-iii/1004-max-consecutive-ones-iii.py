class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_window = 0
        zero_count = 0
        lookup = defaultdict(int)
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            lookup[nums[right]] += 1
            while zero_count > k:
                lookup[nums[left]] -= 1
                if lookup[nums[left]] < 1:
                    del lookup[nums[left]]
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_window = max(max_window, right-left+1)
        return max_window