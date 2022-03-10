class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(start, end):
            if start == end:
                result.append(nums[:])
                return
            for i in range(start, end):
                nums[i], nums[start] = nums[start],nums[i]
                dfs(start+1,end)
                nums[i], nums[start] = nums[start],nums[i]
        
                
        dfs(0,len(nums))
        return result
        
        
#--------------------------------------------------------------------------- 
        # result = []
        # n = len(nums)
        # def backtrack(perm):
        #     if len(perm) == len(nums):
        #         result.append(perm.copy())
        #         return
        #     for i in range(n):
        #         if nums[i] in perm:
        #             continue
        #         perm.append(nums[i])
        #         backtrack(perm)
        #         perm.pop()
        # backtrack([])
        # return result        
              
#--------------------------------------------------------------------------- 
#         result = []
#         if len(nums) == 1:
#             return [nums[:]]
        
#         for i in range(len(nums)):
#             val = nums.pop(0)
#             perms = self.permute(nums)
            
#             for perm in perms:
#                 perm.append(val)
#             result.extend(perms)

#             nums.append(val)
#         return result
                  
#---------------------------------------------------------------------------    
#         def backtrack(start, end):
#             if start == end:
#                 ans.append(nums[:])
#             for i in range(start, end):
                
#                 nums[start], nums[i] = nums[i], nums[start]
                
#                 backtrack(start+1, end)
                
#                 nums[start], nums[i] = nums[i], nums[start]
                
                
#         ans = []
#         backtrack(0, len(nums))
#         return ans
    
        
        
       
        