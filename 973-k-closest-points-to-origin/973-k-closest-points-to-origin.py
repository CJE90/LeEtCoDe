class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        result = []
        
        def distance(x,y):
            return math.sqrt(x*x+y*y)
        
        
        for x,y in points:
            d = distance(x,y)
            heapq.heappush(maxHeap, (-d, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        while maxHeap or len(result) < k:
            _, x, y = heapq.heappop(maxHeap)
            result.append([x,y])
        return result
        
        