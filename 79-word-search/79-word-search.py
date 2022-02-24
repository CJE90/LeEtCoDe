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