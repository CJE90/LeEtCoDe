class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[] for _ in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
       
    
        stack = [source]
        visited = set()
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for i in range(len(adjList[node])):
                    stack.append(adjList[node][i])
            else:
                continue
        return False
            