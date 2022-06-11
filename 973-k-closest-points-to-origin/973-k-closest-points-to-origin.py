class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        for p in points:
            heapq.heappush(max_heap, (self.distance(p)*-1, p))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [points[1] for points in max_heap]
                
    def distance(self, point):
        return sqrt(point[0]*point[0]+point[1]*point[1])