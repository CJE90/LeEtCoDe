# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.existQ = False
        self.existP = False
        result = self.explore(root, p, q)
        return result if self.existQ and self.existP else None
    
    def explore(self, node, p, q):
        if not node:
            return None
        left = self.explore(node.left, p,q)
        right = self.explore(node.right, p, q)
        
        if node == p:
            self.existP = True
            return node
        if node == q:
            self.existQ = True
            return node
        if left and right:
            return node
        return left or right
        
            

