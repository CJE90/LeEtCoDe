# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        min_range = inf
        max_range = -inf
        if not root: return []
        que = deque()
        que.append((root, 0))
        while que:
            node, level = que.popleft()
            min_range = min(min_range, level)
            max_range = max(max_range, level)
            if node.left:
                que.append((node.left, level-1))
            if node.right:
                que.append((node.right, level+1))
            result[level].append(node.val)
        
        


        return [result[x] for x in range(min_range, max_range+1)]
            
        