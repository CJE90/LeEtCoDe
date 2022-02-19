class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        visited = set()
        
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
            
        stack = [(0,-1)]
        while stack:
            curNode, prevNode = stack.pop()
            if curNode in visited:
                return False
            visited.add(curNode)
            for child in adjList[curNode]:
                if child == prevNode:
                    continue
                stack.append((child, curNode))
        return len(visited) == n and True
            
#         def dfs(node, prev):
#             if node == prev:
#                 return True
#             if node in visited:
#                 return False
#             visited.add(node)
#             for child in adjList[node]:
#                 if child != prev:
#                     if not dfs(child, node):
#                         return False
#             return True
#         return dfs(0, -1) and len(visited) == n
            
            
