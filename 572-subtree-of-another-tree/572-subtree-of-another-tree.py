# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        def check_if_equal(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            left = check_if_equal(node1.left, node2.left)
            right = check_if_equal(node1.right, node2.right)
            return left and right
        
        def dfs(node1, node2):
            if not node1:
                return
            if node1.val == node2.val and not self.found:
                if check_if_equal(node1, node2):
                    self.found = True
            dfs(node1.left, node2)
            dfs(node1.right, node2)
            return
        
        dfs(root, subRoot)
        return self.found

        