class Solution {
    public void setZeroes(int[][] matrix) {
        for(int i = 0; i<matrix.length; i++){
            for(int j=0;j< matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    matrix[i][j] = -786;
                }
            }
        }
        
        for(int i = 0; i<matrix.length; i++){
            for(int j=0;j< matrix[0].length; j++){
                if(matrix[i][j] == -786){
                    int horizontal = 0;
                    int vertical = 0;
                    while(horizontal<matrix[0].length){
                        if(matrix[i][horizontal] != -786){
                            matrix[i][horizontal] = 0;
                        }
                        horizontal++;
                    }
                    while(vertical<matrix.length){
                        if(matrix[vertical][j]!= -786){
                            matrix[vertical][j] = 0;
                        }
                        vertical++;
                    }
                    matrix[i][j] = 0;
                }
                
            }
            
        }
        
        
        
    }
}