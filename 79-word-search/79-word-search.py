class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        
        def backtrack(i,j, index):
            if index >= len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visited or word[index] != board[i][j]:
                return False
            visited.add((i,j))
            if (backtrack(i+1,j, index+1) or
                backtrack(i-1,j, index+1) or
                backtrack(i, j+1, index+1) or
                backtrack(i,j-1, index+1)):
                return True
            visited.remove((i,j))
            return False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j, 0):
                        return True
        return False

        