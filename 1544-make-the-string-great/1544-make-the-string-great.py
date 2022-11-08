class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        stack = []
        answer = ""
        #uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #lowers = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            elif ord(s[i])-32 == ord(stack[-1]) or ord(stack[-1])-32 == ord(s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        
        answer = "".join(stack)
        return answer
        
        
        
        
        
        