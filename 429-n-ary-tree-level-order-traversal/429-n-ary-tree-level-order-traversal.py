"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = defaultdict(list)
        if not root: return []
        def explore(node, level):
            if not node:
                return 
            result[level].append(node.val)
            for child in node.children:
                explore(child, level+1)
            return 
        explore(root,0)
        return result.values()

                
        