# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.preorderIndex = 0
        return self.build(0,len(inorder)-1)
    
    def build(self, inStartIndex, inEndIndex):
        if inStartIndex > inEndIndex:
            return None
        root = TreeNode(self.preorder[self.preorderIndex])
        self.preorderIndex += 1
        root.left = self.build(inStartIndex, self.inorder.index(root.val)-1)
        root.right = self.build(self.inorder.index(root.val)+1, inEndIndex)
        return root
        