class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        rowLen = len(grid)
        colLen = len(grid[0])
        que = deque([])
        
        def bfs(grid, que):
            while que:
                I,J = que.popleft()
                for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                    if 0 <= i < rowLen and 0 <= j < colLen and grid[i][j] == "1":
                        que.append((i,j))
                        grid[i][j] = "0"
        
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    que.append((r,c))
                    bfs(grid, que)
                    result += 1
        return result
        
        
        
        
        
        
        
        '''
        class Solution:
    def numIslands(self, grid):
        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.helper(grid,queue) # turn the adjancent '1' to '0'
                    count += 1
        print(grid)
        return count
    
    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0 #0
        '''
        