class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            else:
                if not stack or stack[-1] != s[i]:
                    return False
                stack.pop()
        return len(stack) == 0
                
            
        