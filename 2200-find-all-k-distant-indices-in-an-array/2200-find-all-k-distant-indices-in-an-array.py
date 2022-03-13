class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_vals = []
        result = []
        for i in range(len(nums)):
            if nums[i] == key:
                key_vals.append(i)
        
        for i in range(len(nums)):
            for j in range(len(key_vals)):
                
                if abs(i-key_vals[j]) <= k:
                    result.append(i)
                    break
        return result
        