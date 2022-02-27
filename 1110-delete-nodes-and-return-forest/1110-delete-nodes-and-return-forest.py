# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        
        def deleteNodes(node):
            if not node:
                return None
            node.left = deleteNodes(node.left)
            node.right = deleteNodes(node.right)
            
            if node.val in to_delete:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                return None
            
            return node
            
        deleteNodes(root)
        if root.val not in to_delete:
            result.append(root)
        return result
        