# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subroot:
            return True
        valid = False
        def checkTrees(node, subroot):
            if not node and not subroot:
                return True
            if (node and not subroot) or (subroot and not node) or node.val != subroot.val:
                return False
            return checkTrees(node.left, subroot.left) and checkTrees(node.right, subroot.right)
        
        def exploreParent(node, subroot):
            nonlocal valid
            if not node:
                return 
            if node.val == subroot.val:
                if checkTrees(node, subroot):
                    valid = True
            exploreParent(node.left, subroot)
            exploreParent(node.right,subroot)
            
        
        
        exploreParent(root, subRoot)
        return valid
        
        