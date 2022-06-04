class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N = len(matrix)
        M = len(matrix[0])
        self.presum_matrix = [[0 for _ in range(M+1) ] for _ in range(N+1)]
        for r in range(N):
            prefix = 0
            for c in range(M):
                prefix += matrix[r][c]
                above = self.presum_matrix[r][c+1]
                self.presum_matrix[r+1][c+1] = prefix+above
                
        
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        square = self.presum_matrix[r2][c2]
        left = self.presum_matrix[r2][c1-1]
        top = self.presum_matrix[r1-1][c2]
        corner = self.presum_matrix[r1-1][c1-1]
        return square-top-left+corner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)