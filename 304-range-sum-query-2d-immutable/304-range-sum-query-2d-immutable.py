class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N = len(matrix)
        M = len(matrix[0])
        self.matrix = matrix
        self.forward_matrix = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            temp = 0
            for j in range(M):
                temp += matrix[i][j]
                self.forward_matrix[i][j] = temp


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        offset = col1 - 1
        answer = 0
        for i in range(row1,row2+1):
            answer += self.forward_matrix[i][col2]
            if offset > -1:
                answer -= self.forward_matrix[i][offset]
                # print(i,col2)
                # print(self.forward_matrix[i][col2])
                # print("minus")
                # print(i,offset)
                # print(self.forward_matrix[i][offset])
        return answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



