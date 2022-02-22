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
        
        def dfs(node, string):
            string = string+str(node.val)
            if not node.left and not node.right:
                result.append(int(string))
                return
            if node.left:
                dfs(node.left, string)
            if node.right:
                dfs(node.right, string)
        
        
        dfs(root, "")
        return sum(result)
        