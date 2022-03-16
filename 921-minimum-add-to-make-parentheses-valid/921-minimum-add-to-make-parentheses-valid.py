class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
            if balance == -1:
                result += 1
                balance += 1
        return result + balance
        