class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo = 2
        hi = x // 2 
        while lo <= hi:
            mid = (lo+hi)//2
            n = mid*mid
            if n == x:
                return mid
            elif n > x:
                hi = mid-1
            else:
                lo = mid+1
        return hi
        