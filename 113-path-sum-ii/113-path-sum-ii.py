# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(root, targetSum, path):
            if not root:
                return 
            targetSum -= root.val
            path.append(root.val)
            if not root.left and not root.right and targetSum == 0:
                result.append(path.copy())
            dfs(root.left, targetSum, path)
            dfs(root.right, targetSum, path)
            path.pop()
            return
        dfs(root, targetSum, [])
        return result
            
                
        