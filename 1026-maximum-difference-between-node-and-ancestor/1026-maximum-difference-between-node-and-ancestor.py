# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        
        def dfs(root, lowestFound, highestFound):
            if not root:
                return highestFound-lowestFound
            
            lowestFound = min(root.val, lowestFound)
            highestFound = max(root.val, highestFound)
            
            leftDiff = dfs(root.left, lowestFound, highestFound)
            rightDiff = dfs(root.right, lowestFound, highestFound)
            
            return max(abs(leftDiff), abs(rightDiff))
        return dfs(root, root.val, root.val)
            
        