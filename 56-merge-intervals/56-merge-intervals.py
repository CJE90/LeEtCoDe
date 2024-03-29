class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = []
        
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
        
        
        
        
        
        
        
        
        
        #         intervals.sort(key = lambda x:x[0])
#         result = []
#         for i in intervals:
#             if result and i[0] <= result[-1][1]:
#                 result[-1][1] = max(result[-1][1], i[1])
#             else:
#                 result.append(i)
        
#         return result
        