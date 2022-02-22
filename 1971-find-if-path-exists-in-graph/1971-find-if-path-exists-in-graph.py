class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
            
        def dfs(node) -> bool:
            if node == destination:
                return True
            visited.add(node)
            for child in adjList[node]:
                if child not in visited:
                    if dfs(child):
                        return True
            return False
        
        return dfs(source)
        

        
        
        