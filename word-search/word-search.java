class Solution {
    public boolean exist(char[][] board, String word) {
        int row = board.length;
        int col = board[0].length;
        for(int i = 0; i<row; i++){
            for(int j = 0; j<col; j++){
                if(board[i][j] == word.charAt(0) && backtrack(board, word, i, j, 0)){
                    return true;
                }
            }
        }
        return false;  
    }
    public boolean backtrack(char[][] board, String word, int row, int col, int index){
        if(index>=word.length()){
            return true;
        }
        if(row < 0 || row >= board.length || col < 0 || col >= board[0].length || board[row][col] != word.charAt(index)){
            return false;
        }
        
        boolean foundAValidLetter = false;
        char mark = word.charAt(index);
        board[row][col] = '#';
        
        if(backtrack(board, word, row+1, col, index+1) ||
           backtrack(board, word, row-1, col, index+1) ||
           backtrack(board, word, row, col+1, index+1) ||
           backtrack(board, word, row, col-1, index+1 )){
             foundAValidLetter = true;
        }

        board[row][col] = mark;
        return foundAValidLetter;
    }
}