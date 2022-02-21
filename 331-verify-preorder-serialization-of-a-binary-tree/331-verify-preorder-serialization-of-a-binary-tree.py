class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        v = 1
        for i in preorder.split(','):
            v -= 1
            if v <0:
                return False
            if i != '#':
                v +=2
        return v == 0
        