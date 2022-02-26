# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = deque()
        que = deque()
        
        que.append(root)
        while que:
            n = len(que)
            tmp = deque()
            for _ in range(n):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.appendleft(list(tmp))
        return list(result)
        