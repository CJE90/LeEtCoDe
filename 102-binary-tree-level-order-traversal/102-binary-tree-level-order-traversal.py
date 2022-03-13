# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = defaultdict(list)
        
        def explore(node, level):
            if not node:
                return
            lookup[level].append(node.val)
            explore(node.left, level+1)
            explore(node.right, level+1)
            
                
            
        explore(root, 0)
        
        return lookup.values()
            
        