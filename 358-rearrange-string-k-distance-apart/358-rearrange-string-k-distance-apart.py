class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or k == 1:
            return s
        if len(s) == 0 or len(s) == 1:
            return ""
        lookup = Counter(s)
        maxHeap = [[-cnt, char] for char,cnt in lookup.items()]
        heapq.heapify(maxHeap)
        cooling = {}
        steps = 0
        result = []
        
        while maxHeap:
            
            
            count, char = heapq.heappop(maxHeap)
            result.append(char)
            if count + 1 < 0:
                cooling[char] = [count+1, char]
            if len(result) >= k and result[-k] in cooling:
                previousCount, previousCharacter = cooling.pop(result[-k])
                heapq.heappush(maxHeap, [previousCount, previousCharacter])
            
        return ''.join(result) if len(result)==len(s) else ""   
              
            
    
    
#             if k<=1: 
#             return s
#         d=collections.defaultdict(int)
#         for c in s:
#             d[c]+=1
#         freqs=[[-d[k],k] for k in d]
#         heapq.heapify(freqs)        
#         cooling={}
#         res=[]
#         while freqs:
#             freq,c=heapq.heappop(freqs)
#             res.append(c)
#             freq+=1
#             if freq<0:                
#                 cooling[c]=[freq,c]
#             if len(res)>=k and res[-k] in cooling:
#                 prevFreq,prevC=cooling.pop(res[-k])
#                 heapq.heappush(freqs,[prevFreq,prevC])        
#         return ''.join(res) if len(res)==len(s) else ""
            
        
        
        