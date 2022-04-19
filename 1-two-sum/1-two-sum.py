class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)
        for i,v in enumerate(nums):
            compliment = target-v
            if compliment in lookup:
                return [i,lookup[compliment]]
            lookup[v] = i
        return [-1,-1]
        