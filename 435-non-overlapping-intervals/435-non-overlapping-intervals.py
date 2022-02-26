class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x:x[1])
        end = -inf
        for s,e in intervals:
            if s >= end:
                end = e
            else:
                ans +=1
        return ans
        # ans = 0
        # prevEndTime = -inf
        # intervals.sort(key = lambda x:x[0])
        # for i in intervals:
        #     startTime = i[0]
        #     if startTime >= prevEndTime:
        #         prevEndTime = i[1]
        #     else:
        #         ans +=1
        #         prevEndTime = min(prevEndTime, i[1])
        # return ans
        