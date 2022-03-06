class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        que = deque()
        stop = False
        
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1 or (r,c) in visited:
                return 
            
            que.append((r,c))
            visited.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        def bfs():
            steps = 0
            while que:
                size = len(que)
                
                for _ in range(size):
                    r,c = que.popleft()
                    for newRow, newCol in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                        if 0<=newRow<n and 0<=newCol<n and (newRow,newCol) not in visited:
                            if grid[newRow][newCol] == 1:
                                return steps
                            que.append((newRow,newCol))
                            visited.add((newRow,newCol))
                steps +=1
            return steps
        while not stop:
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i,j)
                        stop = True
                        break
                if stop:
                    break
        return bfs()
                    
        