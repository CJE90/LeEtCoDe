class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        #maxDistance = 0
        rowLen = len(grid)
        colLen = len(grid[0])
        count = 0
        que = deque()
        
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    que.append((r,c))
        
        while que:
            
            size = len(que)
            
            for _ in range(size):
                r,c = que.popleft()
                for direction in ((1,0),(-1,0),(0,1),(0,-1)):
                    newR, newC = r+direction[0], c+direction[1]
                    if newR >= 0 and newR < rowLen and newC >= 0 and newC < colLen and grid[newR][newC] == 0:
                        grid[newR][newC] = 1
                        #maxDistance = max(maxDistance, grid[newR][newC])
                        que.append((newR, newC))
            count+=1
        return count - 1 if count - 1 != 0 else -1
        