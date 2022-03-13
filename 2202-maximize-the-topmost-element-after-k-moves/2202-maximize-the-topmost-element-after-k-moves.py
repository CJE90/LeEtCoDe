class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k%2:
            return -1
        for val, pos in sorted([(element, pos) for pos, element in enumerate(nums)], reverse=True):
            if pos == k or pos < k-1:
                return val
