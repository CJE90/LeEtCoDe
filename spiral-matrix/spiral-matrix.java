class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int r = matrix.length;
        int c = matrix[0].length;
        int westBound = 0;
        int eastBound = c-1;
        int northBound = 0;
        int southBound = r-1;
        
        while(westBound<=eastBound && northBound<=southBound){
            for(int col = westBound; col<=eastBound; col++){
                ans.add(matrix[northBound][col]);
            }
            northBound++;
            for(int row = northBound; row<=southBound; row++){
                ans.add(matrix[row][eastBound]);
            }
            eastBound--;
            for(int col = eastBound; col>=westBound && northBound<=southBound; col--){
                ans.add(matrix[southBound][col]);
            }
            southBound--;
            for(int row = southBound; row>=northBound && westBound<=eastBound; row--){
                ans.add(matrix[row][westBound]);
            }
            westBound++;
        }
        return ans;
        
    }
}