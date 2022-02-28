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
    '''
    1. create hashmap for character frequency
    2. convert that character frequency count to maxHeap
        i. We want to always process the most frequent task
    3. Pop the most frequent task and reduce its count
        i. add it to the que with the time it can be released
    4. increment Time by one becuase we are processing a task
    5. If the task at the head of the que can be processed again. pop it and add it back to the heap
    6. once all task are processed return the time
    '''
            
        
        