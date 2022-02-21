# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        
        def dfs(root, string):
            
            if not root.left and not root.right:
                string = string + str(root.val)
                res.append(string+',')
                
                return
            if root.left:
                dfs(root.left, string)
            if root.right:
                dfs(root.right, string)
            
        dfs(root1,"")
        string1 = ",".join(res)
        res.clear()
        dfs(root2,"")
        string2 = ",".join(res)
        print(string1, string2)
        return string1 == string2
            