# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = []
        result  = []
        if not root:
            return result
        
        que.append(root)
        
        while que:
            tmp = []
            n = len(que)
            for i in range(n):
                node = que.pop(0)
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(tmp)
        return result
        
                
        