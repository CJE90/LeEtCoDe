# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaf_list = []
        
        def getHeight(node):
            if not node:
                return -1
            
            left = getHeight(node.left)
            right = getHeight(node.right)
            curHeight = 1+max(left,right)
            leaf_list.append((node.val, curHeight))
            
            return curHeight
            
        getHeight(root)
        leaf_list.sort(key = lambda x:x[1])
        
        result = [[] for i in range(leaf_list[len(leaf_list)-1][1]+1)]
        for node,level in leaf_list:
            result[level].append(node)
        return result
            
            
        