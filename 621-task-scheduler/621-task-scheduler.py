class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        maxheap = [-cnt for cnt in hm.values()]
        heapq.heapify(maxheap)
        time = 0
        que = deque()
        
        while maxheap or que:
            time += 1
            if maxheap:
                taskCount = 1 + heapq.heappop(maxheap)
            
                if taskCount:
                    que.append([taskCount, time+n])
            if que:        
                possibleTask = que[0]
                if possibleTask[1] == time:
                    heapq.heappush(maxheap, que.popleft()[0])
        
        return time
            
        
        