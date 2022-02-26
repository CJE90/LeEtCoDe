class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        return self.merge(intervals)
            
        
        
        
        
        
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Time Complexity: O(NlogN) logN for the sort and N for the entire walk through intervals array
        Space Complexity: O(N) result array may store every interval in intervals array
        '''
        intervals.sort(key = lambda x:x[0])
        result = []
        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)
        return result
        