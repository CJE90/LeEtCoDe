class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        inDegree = {i:0 for i in range(numCourses)}
        adjList = {i:[] for i in range(numCourses)}
        
        for course, preReq in prerequisites:
            adjList[preReq].append(course)
            inDegree[course] += 1
        
        que = deque()
        for node in inDegree:
            if inDegree[node] == 0:
                que.append(node)
                
        while que:
            node = que.popleft()
            result.append(node)
            for child in adjList[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    que.append(child)
        if len(result) == numCourses:
            return result
        return []
        