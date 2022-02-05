# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder = postorder
        self.inorder = inorder
        self.rootPostOrderIndex = len(postorder)-1
        return self.build(0, len(inorder)-1)
        
    def build(self, inOrderStart, inOrderEnd):
        if inOrderStart > inOrderEnd:
            return None
        root = TreeNode(self.postorder[self.rootPostOrderIndex])
        self.rootPostOrderIndex -= 1
        root.right = self.build(self.inorder.index(root.val)+1, inOrderEnd)
        root.left = self.build(inOrderStart, self.inorder.index(root.val)-1)
        return root
    
        
        
        
        
        
        
        
        
        
        
        