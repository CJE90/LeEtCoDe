"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        if not node:
            return None
        
        def exploreAndCreate(node):
            if node in lookup:
                return lookup[node]
            newNode = Node(node.val)
            lookup[node] = newNode
            for child in node.neighbors:
                newNode.neighbors.append(exploreAndCreate(child))
            return newNode
            
        return exploreAndCreate(node)
    
    
            
      
        
      
        