class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        que = deque()
        steps = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    que.append((i,j))
        
        while que:
            size = len(que)
            
            for _ in range(size):
                r,c = que.popleft()
                for newRow, newCol in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if 0<=newRow<m and 0<=newCol<n and grid[newRow][newCol] == 0:
                        grid[newRow][newCol] = 1
                        que.append((newRow,newCol))
            steps += 1
        return steps-1 if steps - 1 != 0 else -1
        
        