class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        lookup = Counter(s)
        max_heap = []
        for char,cnt in lookup.items():
            heapq.heappush(max_heap, [-cnt, char])
        while max_heap:
            count,char = heapq.heappop(max_heap)
            while count < 0:
                result.append(char)
                count +=1
        return "".join(result)
        
            
        
        














































#         hm = Counter(s)
#         maxHeap = []
#         res = []
#         for key, value in hm.items():
#             heapq.heappush(maxHeap, [-value, key])
#         while maxHeap:
#             c = heapq.heappop(maxHeap)
#             while c[0] < 0:
#                 res.append(c[1])
#                 c[0] += 1
#         return "".join(res)
        
        
        