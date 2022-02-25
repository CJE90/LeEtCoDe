class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)
        
        for index,mgr in enumerate(manager):
            if mgr != -1:
                adjList[mgr].append(index)
        
        def dfs(manager):
            if manager not in adjList:
                return 0
            time = 0
            for emp in adjList[manager]:
                time = max(time, dfs(emp)+informTime[manager])
            return time
            
            
            
            
            
        
        return dfs(headID)
            
        
        