class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return False
        visited = set()
        visiting = set()
        adjList = defaultdict(list)
        
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
            
        def dfs(node):
            if node in visiting:
                return False
            if node not in adjList:
                return True
            visiting.add(node)
            for child in adjList[node]:
                if not dfs(child):
                    return False
            visited.add(node)
            visiting.remove(node)
            adjList[node] = []
            return True
            
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
        
            
        
       