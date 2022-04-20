# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        p = TreeNode()
        c = p
        def dfs(node):
            nonlocal c
            if not node:
                return 
            dfs(node.left)
            c.right = TreeNode(node.val)
            c = c.right
            dfs(node.right)
        dfs(root)
        return p.right
        
        
        