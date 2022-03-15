class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        adjList = defaultdict(list)
        for course,preReq in prerequisites:
            adjList[course].append(preReq)
        visiting = set()
        visited = set()
        result = []
        
        def explore(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for child in adjList[node]:
                
                if not explore(child):
                    return False
                    
            visited.add(node)
            visiting.remove(node)
            result.append(node)
            
            return True
            
        
        for i in range(numCourses):
            if i not in visited:
                if not explore(i):
                    return []
        return result
        