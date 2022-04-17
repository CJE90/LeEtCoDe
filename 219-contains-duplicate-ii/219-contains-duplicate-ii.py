class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for i,v in enumerate(nums):
            if v in lookup and i-lookup[v] <= k:
                return True
            lookup[v] = i
        return False
                
            