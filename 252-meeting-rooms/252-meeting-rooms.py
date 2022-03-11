class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:    
        intervals.sort(key = lambda x : x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                return False
        return True
            
















































#         #intervals.sort(key = lambda x:x[0])
#         prevEnd = -inf
#         for s,e in intervals:
#             if s>=prevEnd:
#                 prevEnd = e
#             else:
#                 return False
#         return True
        