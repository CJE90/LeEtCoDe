class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        
        return self.mergeIntervals(intervals)
        
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         result = []
        
#         for i in intervals:
#             if i[1] < newInterval[0]:
#                 result.append(i)
#             elif newInterval[1] < i[0]:
#                 result.append(newInterval)
#                 newInterval = i
#             else:
#                 newInterval[0] = min(i[0], newInterval[0])
#                 newInterval[1] = max(i[1], newInterval[1])
                
#         result.append(newInterval)
#         return result
        