# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxPath = 0
        
        def explore(node):
            nonlocal maxPath
            if not node:
                return 0
            
            left = explore(node.left)
            right = explore(node.right)
            leftSum = 0
            rightSum = 0
            
            if node.left and node.left.val == node.val:
                leftSum = 1+left
            if node.right and node.right.val == node.val:
                rightSum = 1 + right
            maxPath = max(maxPath, leftSum+rightSum)
            
            
            return max(leftSum, rightSum)
                
        
        explore(root)
        return maxPath
        
        