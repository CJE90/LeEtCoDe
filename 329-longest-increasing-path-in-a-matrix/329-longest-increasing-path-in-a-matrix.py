class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        directions = [(1,0),(-1,0), (0,1),(0,-1)]
        dp = [[None] * C for _ in range(R)]
        
        
        def longestPath(x, y):
            if dp[x][y]:
                return dp[x][y]
            best = 1
            for dx, dy in directions:
                nx = x+dx
                ny = y+dy
                
                if 0 <= nx < R and 0 <= ny < C and matrix[x][y] < matrix[nx][ny]:
                    best = max(best, longestPath(nx,ny)+1)
            dp[x][y] = best       
            return best
        long = 0
        for r in range(R):
            for c in range(C):
                long = max(long, longestPath(r,c))
        return long