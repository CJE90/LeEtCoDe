class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        n = len(matrix)
        for r in range(min(k,n)):
            heapq.heappush(maxHeap, (matrix[r][0], r, 0))
        while k >0:
            element, r, c = heapq.heappop(maxHeap)
            if c+1<len(matrix[0]):
                heapq.heappush(maxHeap, (matrix[r][c+1], r, c+1))
            
            k-=1
        return element
        