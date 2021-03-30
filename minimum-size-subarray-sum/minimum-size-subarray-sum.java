class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        if(nums.length == 0){
            return 1;
        }
        int minWindowSize = Integer.MAX_VALUE;
        int left = 0; int right = 0;
        int currentSum = 0;
        boolean reachedTarget = false;
        
        while(left<=right && right < nums.length){
            currentSum+=nums[right];
            
            while(currentSum >= target){
                reachedTarget = true;
                minWindowSize = Math.min(minWindowSize, right - left +1);
                currentSum -= nums[left];
                left++;
            }
            right++;
        }
        if(reachedTarget){
            return minWindowSize;
        }
        return 0;
        
    }
}