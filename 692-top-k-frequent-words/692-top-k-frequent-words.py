class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = []
        result = []
        lookup = Counter(words)
        for word, cnt in lookup.items():
            heapq.heappush(max_heap, (-cnt, word))
        while k > 0:
            element = heapq.heappop(max_heap)
            result.append(element[1])
            k -= 1
        return result
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxHeap = []
#         result = []
#         lookup = Counter(words)
#         for word,frequency in lookup.items():
#             heapq.heappush(maxHeap, (-frequency, word))
            
#         while maxHeap and len(result) < k:
#             frequency, element = heapq.heappop(maxHeap)
#             result.append(element)
#         return result
        