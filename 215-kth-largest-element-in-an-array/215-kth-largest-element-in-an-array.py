class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

















































#         min_heap = []
#         for num in nums:
#             heapq.heappush(min_heap, num)
#             while len(min_heap) > k:
#                 heapq.heappop(min_heap)
#         return min_heap[0]
        
        