class StockSpanner:
    '''
    [60, 60, ]
    [1,1,1, 2, 1]
    '''
    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans
            
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)