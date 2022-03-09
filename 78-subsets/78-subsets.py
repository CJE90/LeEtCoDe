class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        self.backtrack(nums, result, [])
        return result
    
    def backtrack(self, nums, result, path):
        
        result.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[i+1:], result, path+[nums[i]])
            # path.pop()
        
        
        