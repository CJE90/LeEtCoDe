class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(list)
        count = 0
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        def explore(node):
            if node in visited:
                return
            visited.add(node)
            for child in adjList[node]:
                explore(child)
                
        
        for i in range(n):
            if i not in visited:
                explore(i)
                count += 1
        return count
        
        
        
        
        