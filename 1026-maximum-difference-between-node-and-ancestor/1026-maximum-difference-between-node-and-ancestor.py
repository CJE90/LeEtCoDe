# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, maxVal, minVal):
            if not node:
                return maxVal-minVal
            maxVal = max(maxVal, node.val)
            minVal = min(minVal, node.val)
            leftDiff = dfs(node.left,maxVal, minVal)
            rightDiff = dfs(node.right,maxVal, minVal)
            return max(leftDiff, rightDiff)
        return dfs(root, root.val, root.val)