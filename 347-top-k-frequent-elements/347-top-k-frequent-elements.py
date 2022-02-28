class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = Counter(nums)
        minHeap = []
        result = []
        for element, frequency in lookup.items():
            heapq.heappush(minHeap, (frequency, element))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        while minHeap or len(result) < k:
            _, element = heapq.heappop(minHeap)
            result.append(element)
        return result
        
        