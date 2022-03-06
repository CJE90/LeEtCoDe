class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return 1
        dp = [[0]*n for i in range(m)]
        res_path = []
        
        def dfs(r,c):
            if not dp[r][c]:
                val = matrix[r][c]
                if r and val > matrix[r-1][c]:
                    up = dfs(r-1,c)
                else:
                    up = 0
                if r < m-1 and val > matrix[r+1][c]:
                    down = dfs(r+1,c)
                else:
                    down = 0
                if c and val > matrix[r][c-1]:
                    left = dfs(r,c-1)
                else:
                    left = 0
                if c< n-1 and val > matrix[r][c+1]:
                    right = dfs(r,c+1)
                else:
                    right = 0
                dp[r][c] = 1 + max(up,down,left,right)       
            return dp[r][c]

        
        for r in range(m):
            for c in range(n):
                res_path.append(dfs(r,c))
        print(res_path)
        return max(res_path)
        

