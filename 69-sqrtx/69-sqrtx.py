class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        lo = 1
        hi = x 
        while lo < hi:
            mid = (lo+hi)//2
            if mid*mid > x:
                hi = mid
            else:
                lo = mid+1
        return lo-1
        