class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        chars = list(s)
        
        def backtrack(index):
            result.append("".join(chars))
            for index in range(index, len(chars)):
                if chars[index].isalpha():
                    chars[index] = chars[index].swapcase()
                    backtrack(index+1)
                    chars[index] = chars[index].swapcase()
        
        backtrack(0)
        return result
        
        
        
        
        
#         result = []
#         S = list(s)
        
#         def backtrack(index):
#             result.append(''.join(S))
#             for index in range(index, len(S)):
#                 if S[index].isalpha():
#                     S[index] = S[index].swapcase()
#                     backtrack(index+1)
#                     S[index] = S[index].swapcase()
#         backtrack(0)
#         return result
        
        
        
#         result = []
#         s = s.lower()
        
        
#         def dfs(index, path):
#             if len(path) == len(s):
#                 result.append("".join(path.copy()))
#                 return
#             if s[index].isdigit():
#                 path.append(s[index])
#                 dfs(index+1, path)
#             else:
#                 path.append(s[index])
#                 dfs(index+1, path)
#                 path.pop()
#                 path.append(s[index].upper())
#                 dfs(index+1, path)
#             path.pop()
            
                
            
#         dfs(0, [])
#         return result
        
        
