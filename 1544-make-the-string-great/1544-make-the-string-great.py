class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        stack = []
        answer = ""
        uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if s[i] in uppers and stack[-1] in lowers and stack[-1].upper() == s[i]:
                stack.pop()
            elif s[i] in lowers and stack[-1] in uppers and stack[-1].lower() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        answer = "".join(stack)
        return answer
        
        
        
        
        
        