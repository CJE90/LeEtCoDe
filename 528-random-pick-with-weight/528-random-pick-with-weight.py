class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.totalSum = total
            
        
        

    def pickIndex(self) -> int:
        randChoice = random.randint(1,self.totalSum)
        for index,value in enumerate(self.prefix):
            if randChoice <= value:
                return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()