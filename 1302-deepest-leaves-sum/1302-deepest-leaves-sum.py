# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.sumtoReturn = 0
        def maxDepth(root):
            if not root:
                return 0
            left = 1+maxDepth(root.left)
            right = 1+maxDepth(root.right)
            
            return max(left, right)
        
        def dfs(node, searchDepth):
            if not node:
                return
            if searchDepth == 1:
                self.sumtoReturn += node.val
            
            dfs(node.left, searchDepth-1)
            dfs(node.right, searchDepth-1)
            
        
        searchDepth = maxDepth(root)
        dfs(root, searchDepth)
        return self.sumtoReturn
        