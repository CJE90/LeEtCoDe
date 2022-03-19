# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        if not root:
            return []
        que = deque()
        que.append(root)
        level = 0
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                result[level].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level+= 1
        return result.values()