class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        
        if(image.length == 0 && image[0].length == 0){
            return null;
        }
        
        int val = image[sr][sc];
        dfs(image,sr,sc,newColor,val);
        return image;
        
    }
    
    
    public void dfs(int[][] image, int sr, int sc, int newColor, int val){
        if(image[sr][sc] != val || sr<0 || sr > image.length || sc < 0 || sc>image[0].length || val == newColor){
            return;
        }
        image[sr][sc] = newColor;
        
        if(sr > 0 ){
            dfs(image,sr-1,sc,newColor,val);
        }
        if(sr<image.length-1){
            dfs(image,sr+1,sc,newColor,val);
        }
        if(sc > 0){
            dfs(image,sr,sc-1,newColor,val);
        }
        if(sc<image[0].length-1){
            dfs(image,sr,sc+1,newColor,val);
        }
        
        
    }
}