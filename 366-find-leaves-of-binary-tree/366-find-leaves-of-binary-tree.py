# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = defaultdict(list)
        
        def getHeight(node, level):
            if not node: return 0
            left = getHeight(node.left, level)
            right = getHeight(node.right, level)
            level = max(left,right)
            output[level].append(node.val)
            return level+1
        
        getHeight(root, 0)
        return output.values()