class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            
        def dfs(source, destination, visited):
            if source == destination:
                return True
            if source in visited:
                return False
            
            visited.add(source)
            for child in adjList[source]:
                if dfs(child, destination, visited):
                    return True
            return False
                
        visited = set()
        return dfs(source, destination, visited)
            
            
            