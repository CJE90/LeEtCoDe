class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visited = set()
        adj_list = defaultdict(list)
        for course, pre_req in prerequisites:
            adj_list[course].append(pre_req)
        
        
        def dfs(node):
            if node in visiting:
                return False
            if node not in adj_list:
                return True
            visiting.add(node)
            for neighbors in adj_list[node]:
                if not dfs(neighbors):
                    return False
            visiting.remove(node)
            visited.add(node)
            adj_list[node] = []
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
        
        
        