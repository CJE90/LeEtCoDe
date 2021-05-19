class Solution {
    public int uniquePaths(int m, int n) {
        
        int[][] grid = new int[m+1][n+1];
        
        return helper(m,n,grid);
    
    }
    
    public int helper(int m, int n, int[][] grid){
        if(grid[m][n] != 0){
            return grid[m][n];
        }
        if(m == 1 && n == 1){
            return 1;
        }
        if(m == 0 || n == 0){
            return 0;
        }
        
        grid[m][n] = helper(m-1,n,grid)+helper(m,n-1,grid);
        return grid[m][n];
        
    }
}