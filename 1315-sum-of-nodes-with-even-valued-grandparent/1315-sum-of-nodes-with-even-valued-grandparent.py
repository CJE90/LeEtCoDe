# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        resultSum = 0
        que = deque()
        que.append((root, False))
        
        while que:
            parent, isEvenGrandParent = que.popleft()
            isEvenParent = parent.val % 2 == 0
            for child in parent.left, parent.right:
                if child:
                    que.append((child, isEvenParent))
                    if isEvenGrandParent:
                        resultSum += child.val
        return resultSum
            
        
        
        
        