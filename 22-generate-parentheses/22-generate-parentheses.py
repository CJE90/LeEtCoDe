class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def explore(left, right, path):
            if len(path) == n * 2:
                result.append("".join(path))
                return
            if left < n:
                path.append('(')
                explore(left+1, right, path)
                path.pop()
            if right < left:
                path.append(')')
                explore(left, right+1, path)
                path.pop()
            
        
        explore(0,0,[])
        return result