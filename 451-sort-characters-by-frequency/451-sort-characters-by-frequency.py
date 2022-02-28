class Solution:
    def frequencySort(self, s: str) -> str:
        hm = Counter(s)
        maxHeap = []
        res = []
        for key, value in hm.items():
            heapq.heappush(maxHeap, [-value, key])
        while maxHeap:
            c = heapq.heappop(maxHeap)
            while c[0] < 0:
                res.append(c[1])
                c[0] += 1
        return "".join(res)
        
        
        