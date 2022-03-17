class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                path = ""
                while stack[-1] != '[':
                    path = stack.pop()+ path
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit(): 
                    digit = stack.pop()+digit
                    
                stack.append(path * int(digit))
        return "".join(stack)        
        