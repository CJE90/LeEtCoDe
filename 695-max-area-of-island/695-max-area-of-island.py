class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        currentMax = 0
        
        def count(grid, r, c):
            tempMax = 0
            if r < 0 or r >= rowLen or c < 0 or c >= colLen or grid[r][c] != 1:
                return tempMax
            grid[r][c] = 0
            tempMax += 1
            tempMax += count(grid, r-1, c)
            tempMax += count(grid, r+1, c)
            tempMax += count(grid, r, c-1)
            tempMax += count(grid, r, c+1)
            return tempMax
        
        
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    currentMax = max(count(grid, r, c), currentMax)
        return currentMax
                
        