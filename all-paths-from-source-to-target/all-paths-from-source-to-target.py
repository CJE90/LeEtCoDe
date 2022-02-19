class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        result = []
        
        
        stack = [(0, [0])]
        
        
        
        while stack:
            node, curpath = stack.pop()
            
            if node == target:
                result.append(curpath)
            for child in graph[node]:
                stack.append((child, curpath+[child]))
                
        return result
            
        