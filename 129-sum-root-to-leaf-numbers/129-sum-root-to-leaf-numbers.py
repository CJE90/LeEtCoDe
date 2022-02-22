# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = []
        
        def dfs(node, num):
            num *= 10
            num += node.val
            if not node.left and not node.right:
                result.append(num)
                return
            if node.left:
                dfs(node.left, num)
            if node.right:
                dfs(node.right, num)
        
        
        dfs(root, 0)
        return sum(result)
        