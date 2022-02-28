class Solution:
    def reorganizeString(self, s: str) -> str:
        lookup = Counter(s)
        que = deque()
        maxHeap = []
        result = []
        time = 0
        for letter,frequency in lookup.items():
            heapq.heappush(maxHeap, (-frequency, letter))
        
        while maxHeap or que:
            time +=1
            if maxHeap:
                frequency,letter = heapq.heappop(maxHeap)
                if result and result[len(result)-1] == letter:
                    return ""
                result.append(letter)
                frequency += 1
                if frequency:
                    que.append((frequency, letter, time+1))
                    
            if que and que[0][2] == time:
                frequency,letter, _ = que.popleft()
                heapq.heappush(maxHeap, (frequency, letter))
                
        return "".join(result)
                
                    
        