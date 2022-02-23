class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        
        count = 0
        
        def sink(grid, i, j) -> None:
            if i < 0 or i >= rowLen or j < 0 or j >= colLen or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            sink(grid, i-1, j)
            sink(grid, i+1, j)
            sink(grid, i, j-1)
            sink(grid, i, j+1)
            return
        
        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1":
                    sink(grid, i, j)
                    count += 1
                    
        return count
        
        