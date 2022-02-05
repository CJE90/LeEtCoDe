# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.order = []
        self.inOrderTraversal(root)
        for i in range(len(self.order)-1):
            if self.order[i] >= self.order[i+1]:
                return False
        return True
    def inOrderTraversal(self, node):
        if not node:
            return
        self.inOrderTraversal(node.left)
        self.order.append(node.val)
        self.inOrderTraversal(node.right)
        return
        