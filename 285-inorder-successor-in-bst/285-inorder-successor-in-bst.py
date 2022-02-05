# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.order = []
        self.dfs(root)
        for i in range(len(self.order)-1):
            if self.order[i].val == p.val:
                return self.order[i+1]
        return None
    
    def dfs(self, root):
        if root == None:
            return 
        self.dfs(root.left)
        self.order.append(root)
        self.dfs(root.right)
        return