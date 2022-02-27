class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[1])
        prevEnd = -inf
        for s,e in intervals:
            if s >= prevEnd:
                prevEnd = e
            else:
                return False
        return True
            
        