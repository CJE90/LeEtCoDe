class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        target = (m-1,n-1)
        que = deque([(0,0,k,0)])
        visited = set([(0,0,k)])
        
        while que:
            x,y,eliminated,steps = que.popleft()
            for newRow,newCol in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                
                if 0<=newRow<m and 0<=newCol<n:
                    if grid[newRow][newCol] == 1 and eliminated > 0 and (newRow,newCol, eliminated-1) not in visited:
                        que.append((newRow,newCol, eliminated-1, steps+1))
                        visited.add((newRow,newCol, eliminated-1))
                    if grid[newRow][newCol] == 0 and (newRow, newCol, eliminated) not in visited:
                        if (newRow,newCol) == target:
                            return steps + 1
                        que.append((newRow,newCol, eliminated, steps+1))
                        visited.add((newRow,newCol, eliminated))
        return -1
    
    
    

                
                
                
                
            
        