# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if not root:
            return [""]
        
        def helper(root, string):
            if root == None:
                return
            
            string = string+str(root.val)
            string = string+"->"
            
            if not root.right and not root.left:
                result.append(string[0:len(string)-2])
                return

            if root.left:
                helper(root.left, string)
            if root.right:
                helper(root.right,string)
            
            return
            
        helper(root, "")
        return result
            
        
        