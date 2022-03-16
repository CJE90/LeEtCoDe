class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                stack.append(c)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    count +=1
                    continue
        return count + len(stack)
        