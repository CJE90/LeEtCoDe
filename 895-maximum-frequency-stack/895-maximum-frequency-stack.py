class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.freqStack = defaultdict(list)
        

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        x = self.frequency[val]
        self.freqStack[x].append(val)
        #print(self.frequency)
        #print(self.freqStack)

    def pop(self) -> int:
        x = max(self.frequency.values())
        #print(x)
        item = self.freqStack[x].pop()
        #print(item)
        self.frequency[item] -= 1
        if self.frequency[item] == 0:
            self.frequency.pop(item)
        return item
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()