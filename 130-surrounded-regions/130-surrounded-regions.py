class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return board
        r = len(board)
        c = len(board[0])
        
        def mark(board, row, col):
            if (row < 0 or row >= r or col < 0 or col >= c or board[row][col] != "O"):
                return
            
            board[row][col] = "E"
            mark(board, row-1, col)
            mark(board, row+1, col)
            mark(board, row, col-1)
            mark(board, row, col+1)
            return 
        
        i = 0
        j = 0
        while j<c:
            if board[0][j] == "O":
                mark(board, 0, j)
            if board[r-1][j] == "O":
                mark(board, r-1, j)
            j+=1
        while i< r:
            if board[i][0] == "O":
                mark(board, i, 0)
            if board[i][c-1] == "O":
                mark(board, i, c-1)
            i+=1
            
        i = 0
        j = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'E':
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    
        
        