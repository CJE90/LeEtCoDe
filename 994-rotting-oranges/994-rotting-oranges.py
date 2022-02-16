class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        minutes = 0
        count = 0
        que = deque()
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 2:
                    que.append((r,c))
                elif grid[r][c] == 1:
                    count += 1
        while que:
            n = len(que)
            for _ in range(n):
                r,c = que.popleft()
                for direction in ((1,0),(-1,0),(0,1),(0,-1)):
                    newR, newC = r+direction[0], c+direction[1]
                    if newR >= 0 and newR < rowLen and newC >= 0 and newC < colLen and grid[newR][newC] == 1:
                        count -= 1
                        grid[newR][newC] = 2
                        que.append((newR, newC))
            
            minutes += 1
        if count != 0: return -1
        elif minutes-1 < 0: return 0
        else: return minutes-1
        