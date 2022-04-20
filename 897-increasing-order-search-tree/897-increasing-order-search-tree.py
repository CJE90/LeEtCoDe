# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        p = TreeNode()
        c = p
        for val in result:
            newNode = TreeNode(val)
            c.right = newNode
            c = c.right
        return p.right
        
        