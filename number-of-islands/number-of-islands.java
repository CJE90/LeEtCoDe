class Solution {
    public int numIslands(char[][] grid) {
        //Check edge cases where the grid is empty
        if(grid == null || grid.length == 0){
            return 0;
        }
        //Store the number of columns and Rows
        int numberOfRows = grid.length;
        int numberOfColumns = grid[0].length;
        
        //Initialize the number of Islands to Zero
        int numberOfIslands = 0;

        //walk through every cell in the grid. If "Land" is found we need to sink it
        // or replace it with a zero and then check every other land it touches DFS
        for(int i = 0; i<numberOfRows; i++){
            for(int j = 0; j<numberOfColumns;j++){
                if(grid[i][j] == '1'){
                    //We found some land, increment count and start searching.
                    numberOfIslands++;
                    sink(grid, i, j);
                }
            }
        }
        
        return numberOfIslands;
        
    }
    public void sink(char[][] grid, int row, int col){
        int numberOfRows = grid.length;
        int numberOfColumns = grid[0].length;
        
        //Handle when to return. Either outside of the grid or we did not find land vertically or horizontaly
        if(row<0 || col< 0 || row>=numberOfRows || col >= numberOfColumns || grid[row][col] == '0'){
            return;
        }
        
        //We sink it and then check left, right, down, and up
        grid[row][col] = '0';
        sink(grid,row-1,col);
        sink(grid,row+1, col);
        sink(grid,row,col-1);
        sink(grid,row,col+1);
    }
}