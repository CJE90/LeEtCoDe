class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        n = len(grid)
        que = deque()
        target = (n-1,n-1)
        visited = set()
        steps = 0
        que.append((0,0))
        visited.add((0,0))
        
        while que:
            size = len(que)
            for _ in range(size):
                r,c = que.popleft()
                if (r,c) == target:
                    return steps+1
                for newRow,newCol in [[r-1,c-1],[r-1,c],[r-1,c+1],[r,c-1],[r,c+1],[r+1,c-1],[r+1,c],[r+1,c+1]]:
                    if 0<=newRow<n and 0<=newCol<n and grid[newRow][newCol] == 0 and (newRow,newCol) not in visited:
                        que.append((newRow,newCol))
                        visited.add((newRow,newCol))
                
            steps += 1
            
        return -1
        
        