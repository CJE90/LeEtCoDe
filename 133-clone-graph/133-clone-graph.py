"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
          
        hashTable = {}
        
        def dfs(node) -> 'Node':
            if node in hashTable:
                return hashTable[node]
            copy = Node(node.val)
            hashTable[node] = copy
            for child in node.neighbors:
                copy.neighbors.append(dfs(child))
            return copy
            
        return dfs(node)
        