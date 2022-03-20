"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        result = defaultdict(list)
        level = 0
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                result[level].append(node.val)
                for child in node.children:
                    que.append(child)
            level += 1
        return result.values()
                
        