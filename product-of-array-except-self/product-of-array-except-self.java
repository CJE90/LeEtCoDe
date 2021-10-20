class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        
        result[0] = 1;
        for(int i = 1; i<nums.length; i++){
            result[i] = result[i-1] * nums[i-1];
        }
        int right =1;
        for(int i = result.length-1; i>=0; i--){
            result[i]*=right;
            right*=nums[i];
        }
        return result;
//         int[] forward = new int[nums.length+1];
//         int[] backward = new int[nums.length+1];
//         forward[0] = 1;
//         backward[backward.length-1] = 1;
//          for(int i = 1; i< forward.length; i++){
//              forward[i] = nums[i-1]*forward[i-1];
//          }
//         for(int i = nums.length-1; i>=0; i--){
//             backward[i] = nums[i]*backward[i+1];
//         }
//         for(int i = 0; i< result.length; i++){
//             result[i] = forward[i]*backward[i+1];
//         }
        
//         return result;
    }
}






/*

* 2 6 24        * 24 12 4
1 * 3 12        1 *  12 4
1 2 * 4         2 2  *  4
1 2 6 *         6 6  3  * 1
    
    
    
    0  1  2  3  4
    
    1  1  2  6  24     (i-1)+(i)     
      24 24 12  4  1    
     
       0  1  2  3  4     


    
    (0,1), (1,2), (2,3), (3, 4)
    
    */