from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return 1
        inDegree = defaultdict(int)
        adjList = defaultdict(list)
        steps = 0
        for i in range(m):
            for j in range(n):
                for x,y in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
                    if 0<=x<m and 0<=y<n and matrix[i][j]<matrix[x][y]:
                        adjList[(i,j)].append((x,y))
                        inDegree[(x,y)] += 1
        
        que = deque()
        for node in adjList:
            if node not in inDegree:
                que.append(node)
    
        while que:
            size = len(que)
            steps +=1
            for _ in range(size):
                node = que.popleft()
                for child in adjList[node]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        que.append(child)
            
        return steps
                