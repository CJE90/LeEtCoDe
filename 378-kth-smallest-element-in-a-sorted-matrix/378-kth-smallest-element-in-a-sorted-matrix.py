class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rowLen = len(matrix)
        minHeap = []
        for r in range(min(rowLen, k)):
            heapq.heappush(minHeap, (matrix[r][0], r, 0))
        while k > 0:
            minElement, r, c = heapq.heappop(minHeap)
            if c+1 < len(matrix[0]):
                heapq.heappush(minHeap,(matrix[r][c+1], r, c+1))
            k-=1
        return minElement