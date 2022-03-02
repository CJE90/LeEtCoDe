class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        que = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    que.append([i,j])
        while que:
            x,y = que.popleft()
            for i in range(len(matrix[0])):
                matrix[x][i] = 0
            for j in range(len(matrix)):
                matrix[j][y] = 0
        
        
                              
            
            