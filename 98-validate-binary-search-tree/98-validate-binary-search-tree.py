# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def explore(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            
            left = explore(node.left, lo, node.val)
            right = explore(node.right, node.val, hi)
            return left and right
            
        
        return explore(root, -inf, inf)
        