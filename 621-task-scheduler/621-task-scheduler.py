class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencyTable = Counter(tasks)
        que = deque()
        time = 0
        maxHeap = [[-frequencyTable[key], key] for key,value in frequencyTable.items()]
        
        heapq.heapify(maxHeap)
        
        while maxHeap or que:
            
            if maxHeap:
                count, letter = heapq.heappop(maxHeap)
                if count + 1 < 0:
                    que.append([count+1, letter, time+n])
            if que and que[0][2] == time:
                count, letter, releaseTime = que.popleft()
                heapq.heappush(maxHeap, [count, letter])
            time += 1
        return time
        
            
        
        

    
    















































        
#         lookup = Counter(tasks)
#         que = deque()
#         maxHeap = [-cnt for cnt in lookup.values()]
#         heapq.heapify(maxHeap)
#         time = 0
        
#         while maxHeap or que:
#             time += 1
#             if maxHeap:
#                 task = heapq.heappop(maxHeap)
#                 task += 1
#                 if task:
#                     que.append((task, time+n))
            
#             if que and que[0][1] == time:
#                 taskToAddToHeap = que.popleft()
#                 heapq.heappush(maxHeap,taskToAddToHeap[0])
#         return time
  
#     '''
#     1. create hashmap for character frequency
#     2. convert that character frequency count to maxHeap
#         i. We want to always process the most frequent task
#     3. Pop the most frequent task and reduce its count
#         i. add it to the que with the time it can be released
#     4. increment Time by one becuase we are processing a task
#     5. If the task at the head of the que can be processed again. pop it and add it back to the heap
#     6. once all task are processed return the time
#     '''
            
        
        