# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_found = -inf
        
        def explore(node):
            nonlocal max_found
            if not node:
                return 0
            left = 0
            right = 0
            left = max(explore(node.left), left)
            right = max(explore(node.right), right)
            max_found = max(max_found, node.val+left+right)
            return node.val+max(left,right)
            
        explore(root)
        return max_found
        