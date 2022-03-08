class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        visited = set()
        
        def dfs(r,c,i):
            if i >= len(word):
                return True
            if r < 0 or r >= rowLen or c < 0 or c >= colLen or board[r][c] != word[i] or (r,c) in visited:
                return False
            
            
            visited.add((r,c))
            if (dfs(r+1,c, i+1) or
                    dfs(r-1,c, i+1) or
                    dfs(r,c+1, i+1) or
                    dfs(r, c-1, i+1)):
                return True
            visited.remove((r,c))
            return False
            
        
        
        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False
#         visited = set()
        
#         def backtrack(i,j, index):
#             if index >= len(word):
#                 return True
            
#             if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visited or word[index] != board[i][j]:
#                 return False
#             visited.add((i,j))
#             if (backtrack(i+1,j, index+1) or
#                 backtrack(i-1,j, index+1) or
#                 backtrack(i, j+1, index+1) or
#                 backtrack(i,j-1, index+1)):
#                 return True
#             visited.remove((i,j))
#             return False
            
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     if backtrack(i,j, 0):
#                         return True
#         return False

        