class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                answer.append(interval)
            elif interval[0] > newInterval[1]:
                answer.append(newInterval)
                newInterval = interval
            else:
                newInterval = [min(interval[0],newInterval[0]), max(newInterval[1], interval[1])]
        answer.append(newInterval)
                
        return answer