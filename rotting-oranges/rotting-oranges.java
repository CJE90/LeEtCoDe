class Solution {
    public int orangesRotting(int[][] grid) {
        int[][] directions = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
        int minute = 0;
        int numRows = grid.length;
        int numCols = grid[0].length;
        int freshOranges = 0;
        boolean foundOrange = false;;
        Queue<int[]> que = new LinkedList<>();
        
        for(int i = 0; i<numRows; i++){
            for(int j = 0; j<numCols; j++){
                if(grid[i][j] == 2){
                    que.offer(new int[]{i,j});
                }
                if(grid[i][j] == 1){
                    foundOrange = true;
                    freshOranges++;
                }
            }
        } 
        
        
        while(!que.isEmpty()){
            int n = que.size();
            for(int i = 0; i< n; i++){
                int[] rottingOrange = que.poll();
                for(int[] direction:directions){
                    int newRow = rottingOrange[0]+direction[0];
                    int newCol = rottingOrange[1]+direction[1];
                    
                    if(newRow<0 || newRow>=numRows || newCol<0 || newCol >= numCols || grid[newRow][newCol] != 1){
                        continue;
                    }
                    que.offer(new int[]{newRow, newCol});
                    grid[newRow][newCol] = 2;
                    freshOranges--;
                }
                
            }
            minute++;
        }
        
        if(foundOrange && freshOranges >0) return -1;
        else if(!foundOrange) return 0;
        else return minute-1;
    }
}