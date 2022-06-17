class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(self.doOp(val1, val2, token))
                
            else:
                stack.append(int(token))
        return stack[0]
                
    def doOp(self, val1, val2, operand):
        match operand:
            case '+':
                return val1 + val2
            case '-':
                return val1 - val2
            case '*':
                return val1 * val2
            case '/':
                return int(val1 / val2)
        