class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
















































#         min_heap = []
#         for num in nums:
#             heapq.heappush(min_heap, num)
#             while len(min_heap) > k:
#                 heapq.heappop(min_heap)
#         return min_heap[0]
        
        