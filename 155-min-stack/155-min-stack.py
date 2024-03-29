class MinStack:

    def __init__(self):
        self.stack = []
        self.minTracker = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minTracker or val<=self.minTracker[-1]:
            self.minTracker.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minTracker[-1]:
            self.minTracker.pop()
        return val
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTracker[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()