# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        que = deque()
        que.append(root)
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if i+1 < n:
                        if node.val >= que[0].val:
                            return False
                else:
                    if node.val % 2 != 0:
                        return False
                    if i+1 < n:
                        if node.val <= que[0].val:
                            return False
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level+=1
        return True
                
                
        