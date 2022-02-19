class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        def dfs(node):
            if node in visited:
                return False
            if not adjList[node]:
                return True
            
            visited.add(node)
            for c in adjList[node]:
                if not dfs(c): return False
                
            visited.remove(node)
            adjList[node] = []
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
            
        
        
        