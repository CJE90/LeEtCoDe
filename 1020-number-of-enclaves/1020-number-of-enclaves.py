class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result = 0
        def mark(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                return
            grid[row][col] = -1
            mark(grid, row-1, col)
            mark(grid, row+1, col)
            mark(grid, row, col-1)
            mark(grid, row, col+1)
            return
        r = 0
        while r < len(grid):
            if grid[r][0] == 1:
                mark(grid, r, 0)
            if grid[r][len(grid[0])-1] == 1:
                mark(grid, r, len(grid[0])-1)
            r+=1
        c = 0
        while c < len(grid[0]):
            if grid[0][c] == 1:
                mark(grid, 0, c)
            if grid[len(grid)-1][c] == 1:
                mark(grid, len(grid)-1, c)
            c+=1
        
        for g in grid:
            for v in g:
                if v == 1:
                    result += 1
        return result

        
        
                     
                     