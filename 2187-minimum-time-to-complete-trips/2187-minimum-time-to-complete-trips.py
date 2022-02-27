class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1:
            return time[0]*totalTrips
        lo = 1
        hi = min(time)*totalTrips
        
        while lo < hi:
            mid = lo + (hi - lo) //2
            
            def trip(seconds):
                curSum = 0
                for v in time:
                    curSum += seconds//v
                return curSum >= totalTrips
            
            
            if trip(mid):
                hi = mid
            else:
                lo = mid+1
        return hi