class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        
        def explore(s, path):
            if not s:
                result.append(path[:])
                return
            for i in range(1, len(s)+1):
                if self.isValid(s[:i]):
                    path.append(s[:i])
                    explore(s[i:], path)
                    path.pop()
            
        
        explore(s, [])
        return result
    
    def isValid(self, s):
        lo = 0
        hi = len(s)-1
        while lo<hi:
            if s[lo] != s[hi]:
                return False
            lo+= 1
            hi -=1
        return True
        