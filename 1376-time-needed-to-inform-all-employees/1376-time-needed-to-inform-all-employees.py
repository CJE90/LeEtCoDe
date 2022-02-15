class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n<= 1:
            return 0
        lookup = defaultdict(list)
        for index, mgr in enumerate(manager):
            lookup[mgr].append(index)
        
        def dfs(employee):
            ans = 0
            for developer in lookup[employee]:
                ans = max(ans, dfs(developer)+informTime[employee])
            return ans
        return dfs(headID)
        