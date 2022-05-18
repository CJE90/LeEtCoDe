class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                if stack[-1] != c:
                    return False
                stack.pop()
        return len(stack) == 0
        