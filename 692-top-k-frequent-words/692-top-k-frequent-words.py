class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maxHeap = []
        result = []
        lookup = Counter(words)
        for word,frequency in lookup.items():
            heapq.heappush(maxHeap, (-frequency, word))
            
        while maxHeap and len(result) < k:
            frequency, element = heapq.heappop(maxHeap)
            
            result.append(element)
        return result
        