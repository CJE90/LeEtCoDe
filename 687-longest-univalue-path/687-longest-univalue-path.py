# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxEdges = 0
        
        def dfs(node):
            nonlocal maxEdges
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            leftPath = 0
            rightPath = 0
            if node.left and node.left.val == node.val:
                leftPath  = left + 1
            if node.right and node.right.val == node.val:
                rightPath = right+1
            maxEdges = max(maxEdges, leftPath+rightPath)
            return max(leftPath,rightPath)
            
            
            
        dfs(root)
        return maxEdges
        