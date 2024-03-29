# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0       
        res = []
        self.dfs(root, "", res)
        return sum(res)
    
    def dfs(self, node, path, res):
            if not node.left and not node.right:
                res.append(int(path+str(node.val), base=2))
            if node.left:
                self.dfs(node.left, path+str(node.val), res)
            if node.right:
                self.dfs(node.right, path+str(node.val),res)