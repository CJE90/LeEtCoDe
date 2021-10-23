class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int startCol = 0, startRow = 0, endCol = matrix[0].length-1, endRow = matrix.length-1;
        
        while(startCol<=endCol && startRow<=endRow){
            //moving left to right
            for(int i = startCol; i<=endCol; i++){
                result.add(matrix[startRow][i]);
            }
            startRow++;
            //moving top to bottom
            for(int i = startRow; i<=endRow; i++){
                result.add(matrix[i][endCol]);
            } 
            endCol--;
            //moving right to left
            if(startRow<=endRow){
                for(int i = endCol; i>=startCol; i--){
                result.add(matrix[endRow][i]);
            }
            endRow--;
            }
            
            //moving bottom to top
            if(startCol<=endCol){for(int i = endRow; i>=startRow; i--){
                result.add(matrix[i][startCol]);
            }
            startCol++;}
            
        }
        return result;  
    }
}