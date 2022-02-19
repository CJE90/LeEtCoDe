class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        stack = []
        stack.append(source)
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            
            if node not in visited:
                for child in adjList[node]:
                    stack.append(child)
                    
            visited.add(node)
        return False
        
            
        