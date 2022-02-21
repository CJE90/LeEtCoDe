# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(node, path, curSum):
            curSum += node.val
            if not node.left and not node.right:
                if curSum == targetSum:
                    res.append(path+[node.val])
                return
            if node.left:
                dfs(node.left, path+[node.val], curSum)
            if node.right:
                dfs(node.right, path+[node.val], curSum)
        
        res = []
        dfs(root,[], 0)
        return res