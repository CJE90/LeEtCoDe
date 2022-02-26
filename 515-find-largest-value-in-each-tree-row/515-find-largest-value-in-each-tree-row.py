# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        que = deque()
        que.append(root)
        while que:
            curMax  = -inf
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                curMax = max(curMax, node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(curMax)
        return result
        