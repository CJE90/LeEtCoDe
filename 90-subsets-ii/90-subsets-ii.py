class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        
        def backtrack(index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()
        
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            
            backtrack(index+1)
            
        backtrack(0)
        return result        
        
#         nums.sort()
        
#         result = []
#         subset = []
       
        
#         def dfs(i):
#             if i >= len(nums):
#                 result.append(subset.copy())  
#                 return
            
#             subset.append(nums[i])
#             dfs(i+1)
#             subset.pop()
            
#             while i + 1 < len(nums) and nums[i] == nums[i+1]:
#                 i+=1
#             dfs(i+1)
            
#         dfs(0)
#         return result
        