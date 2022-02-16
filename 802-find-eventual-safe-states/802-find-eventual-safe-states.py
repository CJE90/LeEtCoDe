class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited, result = [-1] * len(graph), []
        def dfs(i):
            visited[i] = 0
            for node in graph[i]:
                if visited[node] == 0 or (visited[node] == -1 and dfs(node)):
                    return True
            visited[i] = 1
            result.append(i)
            return False
        for i in range(len(graph)):
            if visited[i] == -1:
                dfs(i)
        return sorted(result)

    
    '''
    -1 unvisited
     0 visited ( if we encounter a visited while exploring we have found a cycle)
     1 safe
    '''
    
    '''def eventualSafeNodes(self, graph):
        def explore(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
            visited[i] = 1
            res.append(i)
            return False
        visited, res = [-1] * len(graph), []
        for i in range(len(graph)):
            if visited[i] == -1: explore(i)
        return sorted(res)'''
            
        