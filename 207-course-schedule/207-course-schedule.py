class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses ==0:
            return False
        adjList = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1
        
        que = deque()
        for course in indegree:
            if indegree[course] == 0:
                que.append(course)
        
        while que:
            node = que.popleft()
            for child in adjList[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)
        
        for val in indegree:
            if indegree[val] != 0:
                return False
        return True
                
        