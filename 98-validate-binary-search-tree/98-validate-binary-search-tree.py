# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValid(root, -inf, inf)
        
    def isValid(self, node, lowerlimit, upperlimit):
        if node == None:
            return True
        if node.val <= lowerlimit or node.val >= upperlimit:
            return False
        return self.isValid(node.left, lowerlimit, node.val) and self.isValid(node.right, node.val, upperlimit)
        
        