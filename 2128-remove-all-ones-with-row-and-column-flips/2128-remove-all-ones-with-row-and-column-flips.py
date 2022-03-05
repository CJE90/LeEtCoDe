class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for j in range(len(grid[0])):
            if grid[0][j] == 1:
                for i in range(len(grid)):
                    grid[i][j] = 1-grid[i][j]
        print(grid)
        for i in range(1,len(grid)):
            if sum(grid[i]) == 0 or sum(grid[i]) == len(grid[i]):
                continue
            else:
                return False
        return True
                
        
        