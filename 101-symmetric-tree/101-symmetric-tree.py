# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                left_mirror = is_mirror(left.left, right. right)
                right_mirror = is_mirror(left.right, right.left)
                return left_mirror and right_mirror
            else:
                return False
            
        
        return is_mirror(root.left, root.right)
    