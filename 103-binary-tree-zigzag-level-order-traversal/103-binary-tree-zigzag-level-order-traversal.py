# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0
        
        dictLevel = defaultdict(deque)
        que = deque()
        que.append(root)
        
        while que:
            levelSize = len(que)
            for _ in range(levelSize):
                node = que.popleft()
                if level%2 == 1:
                    dictLevel[level].appendleft(node.val)
                else:
                    dictLevel[level].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
        return dictLevel.values()
        