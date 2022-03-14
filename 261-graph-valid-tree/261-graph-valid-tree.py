from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for start,end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        visited  = set()
        
        def explore(node,prev): 
            # if node == prev:
            #     return True
            if node in visited:
                return False
            visited.add(node)
            for child in adjList[node]:
                if child != prev:
                    if not explore(child, node):
                        return False
            return True
        
        return explore(0,-1) and n == len(visited)
        
        
