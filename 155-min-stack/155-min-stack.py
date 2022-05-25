class MinStack:

    def __init__(self):
        self.stack = []
        self.min = inf

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append([val, self.min])

    def pop(self) -> None:
        values = self.stack.pop()
        if not self.stack:
            self.min = inf
        else:
            self.min = self.stack[-1][1]
        return values[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()