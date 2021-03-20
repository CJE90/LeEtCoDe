class Solution {
    public int maxSubArray(int[] nums) {
        
        int finalMax = nums[0];
        int currentSum = finalMax;
        
       for(int i = 1; i< nums.length; i++){
           currentSum = Math.max(currentSum + nums[i], nums[i]);
           finalMax = Math.max(currentSum, finalMax);
       }
        return finalMax;
    }
}