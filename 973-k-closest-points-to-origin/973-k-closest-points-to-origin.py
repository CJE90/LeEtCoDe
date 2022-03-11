class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        min_heap = []
        for point in points:
            heapq.heappush(min_heap, (self.distance(point[0],point[1]), point[0],point[1]))
        while k > 0:
            d, x, y = heapq.heappop(min_heap)
            result.append([x,y])
            k -= 1
        return result
            
    def distance(self, x, y):
        return math.sqrt(x*x+y*y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxHeap = []
#         result = []
        
#         def distance(x,y):
#             return math.sqrt(x*x+y*y)
        
        
#         for x,y in points:
#             d = distance(x,y)
#             heapq.heappush(maxHeap, (-d, x, y))
#             if len(maxHeap) > k:
#                 heapq.heappop(maxHeap)
#         while maxHeap or len(result) < k:
#             _, x, y = heapq.heappop(maxHeap)
#             result.append([x,y])
#         return result
        
        