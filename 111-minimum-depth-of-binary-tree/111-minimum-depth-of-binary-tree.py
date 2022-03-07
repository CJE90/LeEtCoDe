# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(root, level):
            if not root.right and not root.left:
                return level
            right = inf
            left = inf
            if root.left:
                left = helper(root.left, level+1)
            if root.right:
                right = helper(root.right, level+1)
            return min(right,left)
        
        return helper(root,1)