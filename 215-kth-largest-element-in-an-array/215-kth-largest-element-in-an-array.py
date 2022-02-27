class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(k):
            min_heap.append(nums[i])
        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]
                          
        