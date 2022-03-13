class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def dfs(num, path, target):
            if len(path) == k and target == 0:
                result.append(path[:])
            if len(path) > k or target < 0:
                return
            for i in range(num, 10):
                path.append(i)
                dfs(i+1, path, target-i)
                path.pop()
        
        
        dfs(1, [], n)
        return result
        