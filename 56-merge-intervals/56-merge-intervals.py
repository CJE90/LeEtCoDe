class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = []
        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)
        return result
        
        