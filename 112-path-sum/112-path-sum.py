# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = [False]
        
        def dfs(node, curSum):
            curSum += node.val
            if not node.left and not node.right:
                if curSum == targetSum:
                    res[0] = True
                    return
            if node.left:
                dfs(node.left, curSum)
            if node.right:
                dfs(node.right, curSum)
        
        dfs(root, 0)
        return res[0]