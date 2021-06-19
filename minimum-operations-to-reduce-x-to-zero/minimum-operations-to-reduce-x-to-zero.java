class Solution {
    public int minOperations(int[] nums, int x) {
        int sum = 0;
        for(int i = 0; i<nums.length; i++){
            sum += nums[i];
        }
        int target = sum-x;
        
        int left = 0;
        int runningSum = 0;
        int maxLength = -1;
        
        for(int right = 0; right < nums.length; right++){
            runningSum+=nums[right];
            
            while(runningSum > target && left<=right){
                runningSum -= nums[left];
                left++;
            }
            if(runningSum == target){
                maxLength = Math.max(maxLength, right-left+1);
            }
        }
        if(maxLength!=-1){
            return nums.length-maxLength;
        }
        return -1;
        
    }
}