class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        minHeap = []
        for i in intervals:
            if minHeap and i[0]>=minHeap[0]:
                heapq.heapreplace(minHeap, i[1])
            else:
                heapq.heappush(minHeap, i[1])
        return len(minHeap)
        
        
        
        
        
        