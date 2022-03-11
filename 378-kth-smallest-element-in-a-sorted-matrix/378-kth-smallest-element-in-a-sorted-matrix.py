class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        
        for i in range(min(k, len(matrix))):
            heapq.heappush(minHeap, (matrix[i][0], i, 0))
        while k > 0:
            minElement, row, column = heapq.heappop(minHeap)
            
            if column+1 < len(matrix[0]):
                heapq.heappush(minHeap, (matrix[row][column+1], row, column+1))
            k -= 1
        return minElement
        
        
        
        
        
        


















































#         maxHeap = []
#         n = len(matrix)
#         for r in range(min(k,n)):
#             heapq.heappush(maxHeap, (matrix[r][0], r, 0))
#         while k >0:
#             element, r, c = heapq.heappop(maxHeap)
#             if c+1<len(matrix[0]):
#                 heapq.heappush(maxHeap, (matrix[r][c+1], r, c+1))
#             k-=1
#         return element
        