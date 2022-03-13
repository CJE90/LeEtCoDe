class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        
        def dfs(i, path):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(i, n+1):
                path.append(i)
                dfs(i+1,path)
                path.pop()
            return
            
        
        
        dfs(1,[])
        return result