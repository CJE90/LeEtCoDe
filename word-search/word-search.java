class Solution {
    private static int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
    public boolean exist(char[][] board, String word) {
        
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length;j++){
                if(exists(board, i, j, 0, word)){
                    return true;
                }
            }
        }
        return false;
        
    }
    public boolean exists(char[][] board, int row, int col, int index, String word){
        if(index >= word.length()){
            return true;
        }
        
        if(row<0 || row>=board.length || col<0 || col>=board[0].length || board[row][col] != word.charAt(index)){
            return false;
        }
        
        boolean found = false;
        char temp = board[row][col];
        board[row][col] = '#';
        
        for(int[] dir:directions){
            if(exists(board, row+dir[0], col+dir[1], index+1, word)){
                found = true;
            }
        }
        
        board[row][col] = temp;
        return found;
    }
}