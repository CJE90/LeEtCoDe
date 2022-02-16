class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = deque([(headID, 0)])
        result = 0
        graph = defaultdict(list)
        for index, mgr in enumerate(manager):
            graph[mgr].append(index)
        while q:
            curEmp, elapsedTime = q.popleft()
            result = max(result, elapsedTime)
            for subordinate in graph[curEmp]:
                q.append([subordinate, elapsedTime + informTime[curEmp]])
        return result
    
    
    '''
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res
    '''
        