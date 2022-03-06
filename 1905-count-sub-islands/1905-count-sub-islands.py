class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        m = len(grid2)
        n = len(grid2[0])
        count = 0
        self.contained = True
        
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid2[r][c] != 1 or (r,c) in visited:
                return 
            
            visited.add((r,c))
            if grid1[r][c] != grid2[r][c]:
                self.contained = False
                
            dfs(r+1,c) 
            dfs(r-1,c)
            dfs(r,c+1) 
            dfs(r,c-1)
            
            
            
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    self.contained = True
                    dfs(r,c)
                    # print('visiting ')
                    # print(r,c)
                    # print(self.contained)
                    if self.contained:
                        
                        count += 1
        return count
        