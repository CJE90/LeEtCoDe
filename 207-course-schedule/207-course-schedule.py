class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()
        visiting = set()
        for course,preReq in prerequisites:
            adjList[course].append(preReq)
            
        def explore(node):
            if node in visiting:
                return False
            if node not in adjList:
                return True
            visiting.add(node)
            
            for preReq in adjList[node]:
                if not explore(preReq):
                    return False
            #visited.add(node)
            visiting.remove(node)
            adjList[node] = []
            return True
        
        
        for i in range(numCourses):
            if i not in visited:
                if not explore(i):
                    return False
        return True
        
        