class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        rem = 0
        
        while(numBottles+rem>=numExchange):
            ans+=numBottles
            newRem =(numBottles+rem)%numExchange
            numBottles = (numBottles+rem)//numExchange
            rem=newRem 
        ans+=numBottles    
        return ans
        