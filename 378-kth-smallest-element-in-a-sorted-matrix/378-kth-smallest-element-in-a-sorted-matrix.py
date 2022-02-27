class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix[0])
        minHeap = []
        for c in range(min(k,N)):
            #print(matrix[0][N])
            heapq.heappush(minHeap, (matrix[0][c], 0, c))
        
        while k:
            element, r, c = heapq.heappop(minHeap)
            if r < N-1:
                heapq.heappush(minHeap, (matrix[r+1][c], r+1, c))
            k -= 1
        return element
                
                
        