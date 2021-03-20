class Solution {
    public int longestOnes(int[] A, int K) {
        int maxWindowSize = 0;
        int count = 0;
        int l = 0;
        
        for(int r = 0; r< A.length; r++){
            if(A[r] == 0){
                count++;
            }
            while(l <= r && count>K){
                if(A[l] == 0){
                    count--;
                }
                l++;
            }
            maxWindowSize = Math.max(maxWindowSize, r-l+1);
        }
      return maxWindowSize;
    }
}