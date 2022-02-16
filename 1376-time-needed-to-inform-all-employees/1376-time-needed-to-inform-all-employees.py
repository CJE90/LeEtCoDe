class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for emp_index, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(emp_index)
        def dfs(headID):
            ans = 0
            for employee in graph[headID]:
                ans = max(ans, dfs(employee)+informTime[headID])
            return ans
        
        return dfs(headID)
        
        
        
        