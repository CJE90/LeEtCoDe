class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxPath = 0
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        
        def explore(r,c):
            if dp[r][c] > 0:
                return dp[r][c]
            
            for newRow, newCol in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0 <= newRow < len(matrix) and 0<= newCol < len(matrix[0]) and matrix[newRow][newCol]>matrix[r][c]:
                    dp[r][c] = max(dp[r][c], explore(newRow,newCol))
            dp[r][c] += 1
            return dp[r][c]
               
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, explore(r,c))
        print(dp)
        return maxPath
    