class Solution {
    private final int[][] directions = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
    private int numRows;
    private int numCols;
    public void wallsAndGates(int[][] rooms) {
    Queue<int[]> que = new LinkedList<>();
        numRows = rooms.length;
        numCols = rooms[0].length;
        for(int i = 0; i< numRows; i++){
            for(int j = 0; j< numCols; j++){
                if(rooms[i][j] == 0){
                    que.offer(new int[]{i,j});
                }
            }
        }
        
        while(!que.isEmpty()){
            int n = que.size();
            for(int i = 0; i< n; i++){
                int[] cell = que.poll();
                for(int[] direction:directions){
                    int newRow = cell[0] + direction[0];
                    int newCol = cell[1] + direction[1];
                    if(newRow < 0 || newRow >= numRows || newCol < 0 || newCol >= numCols
                      || rooms[newRow][newCol] != Integer.MAX_VALUE){
                        continue;
                    }
                    rooms[newRow][newCol] = rooms[cell[0]][cell[1]] +1;
                    que.add(new int[]{newRow,newCol});
                }
            }
        }
      
    }
    
}