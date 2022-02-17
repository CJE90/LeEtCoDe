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
        return self.binarySearch(self.prefix, randChoice)
        # for index,value in enumerate(self.prefix):
        #     if randChoice <= value:
        #         return index
            
    def binarySearch(self, arr, value) -> int:
        lo = 0
        hi = len(arr)-1
        
        while lo<hi:
            mid = lo + (hi - lo) //2
            if self.prefix[mid] >= value :
                hi = mid
            else:
                lo = mid+1
        return lo
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()