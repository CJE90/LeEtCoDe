class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = sum(piles)
        lo = 1
        
        def isPossible(bananasPerHour) -> bool:
            hoursLeft = h
            for pile in piles:
                testPile = pile
                hoursLeft -= ceil(testPile/bananasPerHour)
                if hoursLeft < 0:
                    return False
            return True
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isPossible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo
        
        
        '''
        Search space is from one to sum
        if hours left after using mid move hi to mid
        what should we do when we run out of time
        l to mid+1
        '''
        
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 24 26 27
#       H         
#       L
# Reurn L
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 24 26 27
# L     M      H                                                         
        
        