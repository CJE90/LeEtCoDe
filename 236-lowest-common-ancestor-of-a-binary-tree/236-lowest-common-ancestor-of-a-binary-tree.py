# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def explore(node):
            
            if node.val == p.val or node.val == q.val:
                return node
            left = right = None
            if node.left:
                left = explore(node.left)
            if node.right:
                right = explore(node.right)
                
            if left and right:
                return node
            else:
                return left or right
            
        
        return explore(root)
            