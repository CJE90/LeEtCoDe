class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #[1,2][2,4][3,6][3,4]
        count = 0
        if not intervals:
            return count
        intervals.sort(key = lambda x : x[1])
        prevEnd = -inf
        for interval in intervals:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                count += 1
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
        