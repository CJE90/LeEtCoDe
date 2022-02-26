# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum  = [0,-inf]
        level = 0
        que = deque()
        que.append(root)
        while que:
            level += 1
            curSum = 0
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                curSum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if curSum > levelSum[1]:
                levelSum[0] = level
                levelSum[1] = curSum
        return levelSum[0]        
        