class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        for index,c in enumerate(s):
            if c != ')':
                stack.append(c)
            else:
                path = []
                while stack[-1] != '(':
                    path.append(stack.pop())
                stack.pop()
                # if index == len(s)-1:
                #     return "".join(path)
                for char in path:
                    stack.append(char)
        return "".join(stack)
        
                
               
               
        