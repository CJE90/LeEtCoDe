# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        def helper(id):
            for i in range(n):
                if id != i:
                    if knows(id, i) or not knows(i,id):
                        return False
            return True
        
        for i in range(n):
            if helper(i):
                return i
        return -1
        