class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        def dfs(source, destination, visited):
            if source == destination:
                return True
            if source in visited:
                return False
            
            visited.add(source)
            for neighbor in adjList[source]:
                if dfs(neighbor, destination, visited):
                    return True
            return False
        visited = set()
        return dfs(source, destination, visited)
            
        
        