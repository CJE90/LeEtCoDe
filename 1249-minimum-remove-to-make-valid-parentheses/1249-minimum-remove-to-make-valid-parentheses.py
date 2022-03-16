class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        bad = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    bad.add(i)
            
        while stack:
            bad.add(stack.pop())
        result = []
        for i in range(len(s)):
            if i not in bad:
                result.append(s[i])
        return "".join(result)