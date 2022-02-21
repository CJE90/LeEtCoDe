# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(root, lo, hi):
            if not root:
                return True
            if root.val <= lo or root.val >= hi:
                return False
            # if root.left and root.val < root.left.val:
            #     return False
            # if root.right and root.val > root.right.val:
            #     return False
            
            
            left = dfs(root.left, lo, root.val)
            right = dfs(root.right, root.val, hi)
            return left and right
        
        return dfs(root, -inf, inf)
        
        
       