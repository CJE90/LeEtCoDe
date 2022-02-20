class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxLen = 0
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for x, y in neighbors:
                    if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[i][j] < matrix[x][y]:
                        graph[(i,j)].append((x,y))
                        indegree[(x,y)]+=1
        
        queue = collections.deque([(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if (i,j) not in indegree])
        while queue:
            maxLen +=1
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                for neighbor in graph[node]:
                    indegree[neighbor]-=1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        return maxLen
        