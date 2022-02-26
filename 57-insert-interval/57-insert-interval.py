class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in intervals:
            if i[1] < newInterval[0]:
                result.append(i)
            elif newInterval[1] < i[0]:
                result.append(newInterval)
                newInterval = i
            elif newInterval[0] <= i[1] or newInterval[1]<=interval[1]:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
                
        result.append(newInterval)
        return result
                
        