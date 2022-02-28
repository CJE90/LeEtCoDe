class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lookup = Counter(tasks)
        que = deque()
        maxHeap = [-cnt for cnt in lookup.values()]
        heapq.heapify(maxHeap)
        time = 0
        
        while maxHeap or que:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    que.append((task, time+n))
            
            if que and que[0][1] == time:
                taskToAddToHeap = que.popleft()
                heapq.heappush(maxHeap,taskToAddToHeap[0])
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
            
        
        