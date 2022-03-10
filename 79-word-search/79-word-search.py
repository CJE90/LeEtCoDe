class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        
        def explore(r, c, index):
            if index >= len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visited or board[r][c] != word[index]:
                return False
            visited.add((r,c))
            
            if (explore(r+1, c, index+1) or
                explore(r-1, c, index+1) or
                explore(r, c+1, index+1) or
                explore(r, c-1, index+1)):
                return True
            visited.remove((r,c))
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if explore(r,c,0):
                        return True
        return False
        