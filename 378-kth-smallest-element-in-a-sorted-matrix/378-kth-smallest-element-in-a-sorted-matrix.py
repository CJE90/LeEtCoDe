class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for row in matrix:
            for col in row:                
                heapq.heappush(maxHeap, col*-1)
                if len(maxHeap)>k:
                    heapq.heappop(maxHeap)
        return maxHeap[0]*-1
                
        