# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longestDiameter = [0]
        
        def edgeCount(node):
            if not node:
                return 0
            left = edgeCount(node.left)
            right = edgeCount(node.right)
            longestDiameter[0] = max(longestDiameter[0], left+right)
            return 1+max(left, right)
        
        edgeCount(root)
        return longestDiameter[0]
        
         
        
            
            
            
            
        
     