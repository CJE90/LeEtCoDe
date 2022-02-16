class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        visited = [-1] * len(graph)
        
        def explore(i):
            visited[i] = 0
            for node in graph[i]:
                if visited[node] == 0 or (visited[node] == -1 and explore(node)):
                    return True
            visited[i] = 1
            result.append(i)
            return False
        
        for i in range(len(graph)):
            if visited[i] == -1:
                explore(i)
        return sorted(result)
        