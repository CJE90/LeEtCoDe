class Solution {
    public int missingNumber(int[] nums) {
        int[] missing = new int[nums.length+1];
        for(int num:nums){
            missing[num] = -1;
        }
        for(int i = 0; i< missing.length; i++){
            if(missing[i] != -1) return i;
        }
        return -1;
        
        
    }
}