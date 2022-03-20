# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        if not root: return []
        que = deque()
        que.append((root, 0))
        while que:
            node, level = que.popleft()
            if node.left:
                que.append((node.left, level-1))
            if node.right:
                que.append((node.right, level+1))
            result[level].append(node.val)
        
        


        t = []
        answer = []
        for key in result.keys():
            t.append(key)
        for key in sorted(t):
            answer.append(result[key])
        return answer
            
        