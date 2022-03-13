class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        
        def explore(s, path, result):
            if not s:
                result.append(path[:])
                return
            for i in range(1, len(s)+1):
                if self.isValid(s[:i]):
                    path.append(s[:i])
                    explore(s[i:], path, result)
                    path.pop()
            
        
        explore(s, [], result)
        return result
    
    def isValid(self, s):
        lo = 0
        hi = len(s)-1
        while lo<hi:
            if s[lo] != s[hi]:
                return False
            lo+= 1
            hi -=1
        return True
        
        
        
#         def partition(self, s):
#         def dfs(s, path, res):
#             if not s:
#                 res.append(path[:])
#                 return
#             for i in range(1, len(s)+1):
#                 if s[:i] == s[i-1::-1]:
#                     path.append(s[:i])
#                     dfs(s[i:], path, res)
#                     path.pop()        
#         res = []
#         dfs(s, [], res)
#         return res