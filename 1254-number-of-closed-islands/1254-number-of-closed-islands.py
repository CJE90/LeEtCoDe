class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rowLen = len(grid)
        colLen = len(grid[0])
        ans = 0
        i, j = 0, 0
        
        def mark(grid, r, c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen or grid[r][c] != 0:
                return 
            grid[r][c] = -1
            mark(grid, r-1, c)
            mark(grid, r+1, c)
            mark(grid, r, c-1)
            mark(grid, r, c+1)
            return
        
        
        while i<rowLen:
            mark(grid, i, 0)
            mark(grid, i, colLen-1)
            i += 1
        while j<colLen:
            mark(grid, 0, j)
            mark(grid, rowLen-1, j)
            j += 1
        print(grid)
        for r in range(1, rowLen):
            for c in range(1, colLen):
                if grid[r][c] == 0: 
                    mark(grid, r, c)
                    ans += 1
        return ans
        
        