class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        self.backtrack(nums, result, [])
        return result
    
    def backtrack(self, nums: List[int], result: List[int], path: List[int]):
        
        result.append(path.copy())
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[i+1:], result, path)
            path.pop()
        
        
        