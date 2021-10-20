class Solution {
    public void setZeroes(int[][] matrix) {
        ArrayList<Integer> rows = new ArrayList<>();
        ArrayList<Integer> cols = new ArrayList<>();
        for(int i = 0; i< matrix.length; i++){
            for(int j = 0; j<matrix[0].length;j++){
                if(matrix[i][j] == 0){
                    rows.add(i);
                    cols.add(j);
                    //break;
                }
            }
        }
        
        for(Integer num:rows){
            for(int i = 0; i<matrix[0].length; i++){
                matrix[num][i] = 0;
            }
        }
        for(Integer num:cols){
            for(int i = 0; i<matrix.length; i++){
                matrix[i][num] = 0;
            }
        }
        
    }
}