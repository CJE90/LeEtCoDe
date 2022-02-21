# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum >= limit
            left = dfs(node.left, curSum)
            right = dfs(node.right, curSum)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right
                
           
        result = dfs(root, 0)
        return root if result else None
        
        
