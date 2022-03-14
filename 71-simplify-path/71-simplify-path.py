class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitPath = path.split('/')
        
        
        for val in splitPath:
            if val == '' or val == '.':
                continue
            elif val == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(val)
        return "/"+"/".join(stack)
                
            