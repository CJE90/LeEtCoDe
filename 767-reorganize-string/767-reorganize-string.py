class Solution:
    def reorganizeString(self, s: str) -> str:
        
        lookup = Counter(s)
        max_heap = []
        que = deque()
        result = []
        step = 0
        for character,count in lookup.items():
            heapq.heappush(max_heap, (-count, character))
        while max_heap or que:
            step += 1
            if max_heap:
                count,character = heapq.heappop(max_heap)
                if result and result[-1] == character:
                    return ""
                result.append(character)
                if count+1 < 0:
                    que.append((count+1, character, step+1))
            
            if que:
                if que[0][2] == step:
                    count, character, _  = que.popleft()
                    heapq.heappush(max_heap, (count, character))
        return "".join(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         lookup = Counter(s) #O(n)
#         que = deque()
#         maxHeap = []
#         result = []
#         time = 0
#         for letter,frequency in lookup.items(): #O(n)
#             heapq.heappush(maxHeap, (-frequency, letter))
        
#         while maxHeap or que:#O(n)
#             time +=1
#             if maxHeap:
#                 frequency,letter = heapq.heappop(maxHeap)
#                 if result and result[len(result)-1] == letter:
#                     return ""
#                 result.append(letter)
#                 frequency += 1
#                 if frequency:
#                     que.append((frequency, letter, time+1))
                    
#             if que and que[0][2] == time:
#                 frequency,letter, _ = que.popleft()
#                 heapq.heappush(maxHeap, (frequency, letter))
                
#         return "".join(result)
                
                    
        