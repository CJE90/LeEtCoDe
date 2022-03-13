# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = 0
        
        def explore(node):
            nonlocal result
            nonlocal k
            if not node:
                return 
            explore(node.left)
            k -= 1
            if k == 0:
                result = node.val
                return
            
            explore(node.right)
            
        explore(root)
        return result
            