# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, inf, -inf)
        
    def isValid(self, node, upper, lower):
        if not node:
            return True
        if node.val >= upper or node.val <= lower:
            return False
        return self.isValid(node.left, node.val, lower) and self.isValid(node.right,upper, node.val )
    
    
        