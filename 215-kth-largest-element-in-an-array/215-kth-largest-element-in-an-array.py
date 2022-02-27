class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, n*-1)
        val = -inf
        for i in range(k):
            val = heapq.heappop(maxHeap)
        return val * -1
