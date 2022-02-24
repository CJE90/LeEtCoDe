class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        perm = []
        unused = set(nums)
        def backTrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return result
        
            for num in list(unused):
                perm.append(num)
                unused.remove(num)
                backTrack()
                perm.pop()
                unused.add(num)
    
        backTrack()
        return result
            
            
            
            
       
        
        
       
        