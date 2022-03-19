class FreqStack:

    def __init__(self):
        self.freqCount = defaultdict(int)
        self.freqStack = defaultdict(list)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        self.freqCount[val] += 1
        x = self.freqCount[val]
        self.freqStack[x].append(val)
        self.maxFreq = max(self.maxFreq, x)
        

    def pop(self) -> int:
        x = self.maxFreq
        
        item = self.freqStack[x].pop()
        self.freqCount[item] -= 1
        if self.freqCount[item] == 0:
            self.freqCount.pop(item)
        if len(self.freqStack[x]) == 0:
            self.maxFreq -= 1
        return item
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()