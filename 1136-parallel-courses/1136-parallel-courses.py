class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        semesters = 0
        que = deque()
        adjList = {i:[] for i in range(1,n+1)}
        inDegree = {i:0 for i in range(1,n+1)}
        for prevCourse, reqCourse in relations:
            adjList[prevCourse].append(reqCourse)
            inDegree[reqCourse] += 1
        for node in inDegree:
            if inDegree[node] == 0:
                que.append(node)
        while que:
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                for child in adjList[node]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        que.append(child)
            semesters += 1
            
            
        for node in inDegree:
            if inDegree[node] != 0:
                return -1
        return semesters