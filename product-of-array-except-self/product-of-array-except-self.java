class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] forward = new int[nums.length+1];
        int[] backward = new int[nums.length+1];
        int[] result = new int[nums.length];
        forward[0] = 1;
        backward[backward.length-1] = 1;
        int sum = 1;
        for(int i = 0; i< nums.length; i++){
            sum*=nums[i];
            forward[i+1]= sum;
        }
        sum = 1;
        for(int i = backward.length-2;i>=0; i--){
            sum*=nums[i];
            backward[i] = sum;
        }
        
        for(int i = 0; i<result.length; i++){
            result[i] = forward[i]*backward[i+1];
        }
        
        return result;
    }
    
}







       //         4   5   1   8   2   10   6
       //      1  4  20   20 160 320 3200 19200
       //      19200 4800 960 960 120  60   6   1