class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    que.append([i,j])
                else:
                    mat[i][j] = -1
        while que:
            r,c = que.popleft()
            for newR,newC in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0 <= newR < len(mat) and 0 <= newC < len(mat[0]) and mat[newR][newC] == -1:
                    mat[newR][newC] = mat[r][c] + 1
                    que.append([newR,newC])
                    
        return mat
        