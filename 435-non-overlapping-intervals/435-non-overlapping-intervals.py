class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        prevEnd = -inf
        count = 0
        for s,e in intervals:
            if s>=prevEnd:
                prevEnd = e
            else:
                count += 1
        return count
        