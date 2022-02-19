class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        que = deque()
        que.append(source)
        
        while que:
            node = que.popleft()
            if node == destination:
                return True
            visited.add(node)
            for child in adjList[node]:
                if child not in visited:
                    que.append(child)
        return False
            
        
            
        