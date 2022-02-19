class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        visited = set()
        prev = -1
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
            
        def dfs(node, prev):
            if node == prev:
                return True
            if node in visited:
                return False
            visited.add(node)
            for child in adjList[node]:
                if child != prev:
                    if not dfs(child, node):
                        return False
            return True
        return dfs(0, -1) and len(visited) == n
            
            
#         def dfs(node):
#             if node in visited:
#                 return False
#             visited.add(node)
            
#             for child in adjList[node]:
#                 if self.prev != child:
#                     self.prev = node
#                     if not dfs(child):
#                         return False
#             return True
                    
            
            
#         return dfs(0) and len(visited) == n
        