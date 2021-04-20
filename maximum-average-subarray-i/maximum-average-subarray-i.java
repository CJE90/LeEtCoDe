class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        double maxAverage = Integer.MIN_VALUE;
        int left = 0;
        double curSum = 0;
        
        for(int right = 0; right < nums.length; right++){
            curSum += nums[right];
             while(right - left + 1 >= k){
                 maxAverage = Math.max(maxAverage, (curSum / k));
                 curSum -= nums[left];
                 left++;
             }
        }
        return maxAverage;
        
    }
}