class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            que = deque()
            visited = set()
            steps = 0
            que.append((r,c))
            visited.add((r,c))
            
            while que:
                n = len(que)
                
                #print(que)
                for _ in range(n):
                    x,y = que.popleft()
                    if grid[x][y] == '#':
                        return steps
                    for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                        newX = x+i
                        newY = y+j
                        if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and (newX,newY) not in visited and grid[newX][newY] != 'X': 
                            visited.add((newX,newY))
                            que.append((newX,newY))    
                steps +=1
            return -1                                                                      
                                                                                       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    return bfs(i,j)
        
        
        
        
                    
        