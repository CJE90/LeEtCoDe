class Solution {
    private final int[][] direction = {{0,1},{0,-1},{1,0},{-1,0}};
    public boolean exist(char[][] board, String word) {
        int rowLength = board.length;
        int colLength = board[0].length;
        
        for(int i = 0 ; i <rowLength; i++){
            for(int j = 0 ; j < colLength; j++){
                if(board[i][j] == word.charAt(0) && exists(board, i, j, 0, word)){
                    return true;
                }
            }
        }
        return false;
        
    }
    
    public boolean exists(char[][]board, int row, int col, int index, String word){
        if(index>=word.length()){
            return true;
        }
        if(row<0 || row>= board.length || col<0 || col>= board[0].length || word.charAt(index) != board[row][col]){
            return false;
        }
        
        char temp = board[row][col];
        board[row][col] = '#';
        
        boolean found = false;
        
        for(int[] d:direction){
            if(exists(board, row+d[0], col+d[1], index+1, word)){
                found = true;
                break;
            }
        }
        board[row][col] = temp;
        return found;
    }
}