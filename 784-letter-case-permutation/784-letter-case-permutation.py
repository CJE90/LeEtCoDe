class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        s = s.lower()
        
        
        def dfs(index, path):
            if len(path) == len(s):
                result.append("".join(path.copy()))
                return
            if s[index].isdigit():
                path.append(s[index])
                dfs(index+1, path)
            else:
                path.append(s[index])
                dfs(index+1, path)
                path.pop()
                path.append(s[index].upper())
                dfs(index+1, path)
            path.pop()
            
                
            
        dfs(0, [])
        return result
        
        
