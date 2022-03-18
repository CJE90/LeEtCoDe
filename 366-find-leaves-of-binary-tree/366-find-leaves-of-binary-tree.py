# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        
        def explore(node):
            if not node:
                return 0
            left = explore(node.left)
            right = explore(node.right)
            height = 1+max(left,right)
            levels[height].append(node.val)
            return height
        explore(root)
        return levels.values()