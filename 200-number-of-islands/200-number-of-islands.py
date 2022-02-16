class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rowLen = len(grid)
        colLen = len(grid[0])
        result = 0
        
        def dfs(grid, r, c):
            if r < 0 or r>= rowLen or c < 0 or c >= colLen or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
            return
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    result += 1
        return result
            
        
        
        