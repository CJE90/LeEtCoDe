class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #[[1,100],[11,22],[1,11],[2,12]]
        # 1,100 1,11 2,12 11,22
        count = 0
        if not intervals:
            return count
        intervals.sort(key = lambda x : x[0])
        prevEnd = -inf
        for interval in intervals:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                count += 1
                prevEnd = min(prevEnd, interval[1])
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         intervals.sort(key = lambda x:x[1])
#         prevEnd = -inf
#         count = 0
#         for s,e in intervals:
#             if s>=prevEnd:
#                 prevEnd = e
#             else:
#                 count += 1
#         return count
        