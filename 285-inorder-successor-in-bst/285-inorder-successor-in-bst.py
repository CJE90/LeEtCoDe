# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        curr=root
        stack=[]
        turn=False
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            # curr=None
            # stack top is the left most
            node=stack.pop()
            if node.right:
                curr=node.right
                
            if turn:
                return node
            
            if node==p:
                turn=True