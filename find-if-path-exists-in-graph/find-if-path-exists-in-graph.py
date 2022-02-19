class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            
            for child in adjList[node]:
                if dfs(child):
                    return True
            return False
        
        return dfs(source)
        
            
        