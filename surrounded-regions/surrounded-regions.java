class Solution {
    private final int[][] directions = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
    private int numRows;
    private int numCols;
    public void solve(char[][] board) {
        int numRows = board.length;
        int numCols = board[0].length;
        
        
        List<int[]> borderCells = new ArrayList<>();
        for(int i = 0; i<numRows;i++){
            int[] col1 = new int[]{i,0};
            int[] lastCol = new int[]{i, numCols-1};
            borderCells.add(col1);
            borderCells.add(lastCol);
        }
        for(int j = 1; j<numCols-1; j++){
            int[] firstRow = new int[]{0,j};
            int[] lastRow = new int[]{numRows-1, j};
            borderCells.add(firstRow);
            borderCells.add(lastRow);
        }
       
        // for(int[] cell:borderCells){
        //     System.out.println("<"+cell[0]+","+cell[1]+">");
        // }
        for(int[] cell:borderCells){
            
            if(board[cell[0]][cell[1]] == 'O'){
                dfs(board, cell[0], cell[1], numRows, numCols);
            }
        }
        
        for(int i = 0; i< numRows; i++){
            for(int j = 0; j<numCols; j++){
                if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if(board[i][j] == 'M'){
                    board[i][j] = 'O';
                }
            }
        }
        
    }
    
    public void dfs(char[][] board, int row, int col, int numRows, int numCols){
        
        if(row < 0 || row >= numRows || col < 0 || col >= numCols || board[row][col] == 'X' || board[row][col] == 'M'){
            return;
        }
        // System.out.println("row: "+row);
        // System.out.println("col: "+col);
        board[row][col] = 'M';
        for(int[] direction:directions){
            int newRow = row+direction[0];
            int newCol = col+direction[1];
            //System.out.println("Calling DFS on Row: "+newRow+" and Col: "+newCol);
            dfs(board, newRow, newCol, numRows, numCols);
        }
    }
}