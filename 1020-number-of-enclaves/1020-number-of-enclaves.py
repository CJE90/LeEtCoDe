class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.count = 0
        visited = set()
        
        def exploreAndCount(r,c,countModifier):
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visited or grid[r][c] != 1:
                return 
            visited.add((r,c))
            self.count += countModifier
            exploreAndCount(r+1,c,countModifier)
            exploreAndCount(r-1,c,countModifier)
            exploreAndCount(r,c+1,countModifier)
            exploreAndCount(r,c-1,countModifier)
            return
        
        for r in range(len(grid)):
            if grid[r][0] == 1:
                exploreAndCount(r,0,0)
            if grid[r][len(grid[0])-1] == 1:
                exploreAndCount(r,len(grid[0])-1, 0)
        for c in range(len(grid[0])):
            if grid[0][c] == 1:
                exploreAndCount(0,c,0)
            if grid[len(grid)-1][c] == 1:
                exploreAndCount(len(grid)-1, c, 0)
        
        for r in range(1,len(grid)-1):
            for c in range(1,len(grid[0])-1):
                if grid[r][c] == 1:
                    exploreAndCount(r,c,1)
        return self.count
            