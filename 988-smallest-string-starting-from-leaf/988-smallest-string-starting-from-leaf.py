# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        def dfs(node, path):
            path = path +chr(ord('a')+node.val)
            if not node.left and not node.right:
                if res[0] == None:
                    res[0] = path[::-1]
                else:
                    res[0] = min(res[0], path[::-1])
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right,path)
        
        res = [None]
        dfs(root,'')
        return res[0]
        
        
        
        
