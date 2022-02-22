class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        
        def dfs(node, curPath) -> None:
            curPath.append(node)
            if node == len(graph)-1:
                result.append(curPath.copy())
                return
            for child in graph[node]:
                dfs(child, curPath)
                curPath.pop()
            
                
            
        
        dfs(0, [])
        return result
        