class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = Counter(nums)
        min_heap = [[-lookup[key], key] for key in lookup.keys()]
        heapq.heapify(min_heap)
        result = []
        while k > 0:
            frequency, character = heapq.heappop(min_heap)
            result.append(character)
            k -= 1
        return result
        
        

















































#         lookup = Counter(nums)
#         minHeap = []
#         result = []
#         for element, frequency in lookup.items():
#             heapq.heappush(minHeap, (frequency, element))
#             if len(minHeap) > k:
#                 heapq.heappop(minHeap)
#         while minHeap or len(result) < k:
#             _, element = heapq.heappop(minHeap)
#             result.append(element)
#         return result
        
        