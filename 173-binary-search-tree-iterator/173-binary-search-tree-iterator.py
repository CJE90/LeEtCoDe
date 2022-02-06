# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.arr = []
        self.index = -1
        self.dfs(root)
    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)
        return
        
        

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        if self.index+1 >= len(self.arr):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()