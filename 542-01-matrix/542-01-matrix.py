class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque()
        rowLen = len(mat)
        colLen = len(mat[0])
        
        for i in range(rowLen):
            for j in range(colLen):
                if mat[i][j] == 0:
                    que.append((i,j))
                else:
                    mat[i][j] = -1
        
        while que:
            r,c = que.popleft()
            for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
                newR, newC = r+direction[0], c+direction[1]
                if newR >= 0 and newR < rowLen and newC >= 0 and newC < colLen and mat[newR][newC] == -1:
                    mat[newR][newC] = mat[r][c] + 1
                    que.append((newR, newC))
        return mat
            
            
        '''visited = set()
        from collections import deque
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
                        matrix[newX][newY] = matrix[x][y] + 1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        return matrix'''
        