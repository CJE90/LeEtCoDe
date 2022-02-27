class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        minHeap = []
        result = []
        for key in hm:
            heapq.heappush(minHeap, (hm[key], key))
            print(minHeap)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        while minHeap:
            obj = heapq.heappop(minHeap)
            result.append(obj[1])
        return result
        