# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if not root:
            return res
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
        return res
        