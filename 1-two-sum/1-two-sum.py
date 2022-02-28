class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int)
        result = []
        for i,v in enumerate(nums):
            compliment = target-v
            if compliment in hm:
                result.append(i)
                result.append(hm[compliment])
            hm[v] = i
        return result
            
            
        