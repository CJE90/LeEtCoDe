"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        lookup = {}
        
        def dfs(node):
            if node in lookup:
                return lookup[node]
            newNode = Node(node.val)
            lookup[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)
        