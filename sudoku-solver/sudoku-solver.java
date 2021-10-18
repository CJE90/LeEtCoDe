class Solution {
    public void solveSudoku(char[][] board) {
        if(board == null || board.length == 0){
            return;
        }
        solve(board);
    }
    
    public boolean solve(char[][] board){
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j] == '.'){
                    for(char guess = '1'; guess<= '9'; guess++){
                        if(isValid(board, i, j, guess)){
                            board[i][j] = guess;
                            if(solve(board))
                                return true;
                            else
                                board[i][j] = '.';
                        }
                        
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    private boolean isValid(char[][] board, int row, int col, char c) {
    for(int i=0; i<9; i++) {
        if(board[i][col] != '.' && board[i][col] == c) return false;
        if(board[row][i] != '.' && board[row][i] == c) return false;
        if(board[3*(row/3)+i/3][3*(col/3)+i%3] != '.' && board[3*(row/3)+i/3][3*(col/3)+i%3] == c) return false;
    }
    return true;
}
}