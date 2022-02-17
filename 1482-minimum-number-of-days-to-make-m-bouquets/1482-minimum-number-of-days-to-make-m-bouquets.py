class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        hi = max(bloomDay)
        lo = 1
        
        def feasible(days) -> bool:
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m
    
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo
        
        '''
        if possible set hi to mid
        lo = mid + 2
        
        '''
# [1,10,2,9,3,8,4,7,5,6]        
        
# 1 2 3 4 5 6 7 8 9 10        
#                 L  H        
#                 M
