class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if(nums.length == 1 || nums.length == 0){
            return nums.length;
        }
        
        int maxCount = 0;
        int currCount = 1;
        
        for(int i = 1; i<nums.length;i++){
            if(nums[i]>nums[i-1]){
                currCount++;
            }
            else{
                maxCount = Math.max(maxCount, currCount);
                currCount = 1;
            }
        }
        
        return Math.max(maxCount, currCount);
        
    }
}