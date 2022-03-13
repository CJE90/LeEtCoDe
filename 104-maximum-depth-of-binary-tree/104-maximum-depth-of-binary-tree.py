# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            curDepth, node = stack.pop()
            if node:
                depth = max(curDepth, depth)
                if node.left:
                    stack.append((curDepth+1, node.left))
                if node.right:
                    stack.append((curDepth + 1, node.right))
        return depth
        