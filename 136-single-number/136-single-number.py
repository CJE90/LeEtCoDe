class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for val in nums:
            if val in seen:
                seen.remove(val)
            else:
                seen.add(val)
        return seen.pop()
        