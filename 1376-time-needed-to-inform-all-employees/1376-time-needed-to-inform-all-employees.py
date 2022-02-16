class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        self.result = 0
        for emp_index, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(emp_index)
        def dfs(headID, time):
            # ans = 0
            # for employee in graph[headID]:
            #     ans = max(ans, dfs(employee)+informTime[headID])
            # return ans
            self.result = max(self.result, time)
            for emp in graph[headID]:
                dfs(emp, time+informTime[headID])
            return self.result
            
            
            
        result = dfs(headID, 0)
        return result
        
        
        
        