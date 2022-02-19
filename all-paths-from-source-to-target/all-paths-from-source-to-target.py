class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        result = []
        path = []
        
        def dfs(node):
            path.append(node)
            if node == target:
                result.append(path.copy())
                return
            for child in graph[node]:
                dfs(child)
                path.pop()
            return
            
        dfs(0)
        return result
        