# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def findMaxDiff(node: TreeNode, lo: int, hi: int) -> int:
            if not node:
                return hi-lo
            hi = max(hi, node.val)
            lo = min(lo, node.val)
            left = findMaxDiff(node.left, lo, hi)
            right = findMaxDiff(node.right, lo,hi)
            return max(left,right)
            
            
        return findMaxDiff(root, inf, -inf)
            