class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        result = []
        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt(x*x+y*y)
            heapq.heappush(maxHeap, (-distance, x, y))
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        for point in maxHeap:
            result.append([point[1], point[2]])
        return result
        
            
        