class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        visited = set()
        visiting = set()
        adjList = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
            
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            # if adjList[node] == []:
            #     result.append(node)
            #     visited.add(node)
            #     return True
            visiting.add(node)
            for prereq in adjList[node]:
                if not dfs(prereq):
                    return False
                
            visiting.remove(node)
            result.append(node)
            visited.add(node)
            #adjList[node] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
        
        
        
