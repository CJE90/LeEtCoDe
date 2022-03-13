# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        
        def explore(node):
            
            if not node:
                result.append('N')
                return
            result.append(str(node.val))
            explore(node.left)
            explore(node.right)
        explore(root)
        
        return ",".join(result)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        path = data.split(',')
        self.i = 0
        def explore():
            if path[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(path[self.i]))
            self.i += 1
            node.left = explore()
            
            node.right = explore()
            return node
        return explore()
            
            
                
            
         
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))