class Solution {
    public void rotate(int[][] matrix) {
        int l = 0, r = matrix[0].length-1;
        int temp;
        
        while(l< r){
            
            for(int i = 0; i<r-l; i++){
                int top = l, bottom = r;
                //store top left value
                temp = matrix[top][l+i];
                //move bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l];
                //move bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i];
                //move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r];
                //move temp to top right
                matrix[top+i][r] = temp;
            }
            l++;
            r--;
        }
        
    }
}