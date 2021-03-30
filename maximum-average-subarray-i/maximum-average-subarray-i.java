class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        double maxAverage = Integer.MIN_VALUE;
        int left = 0;
        int right = 0;
        double currSum = 0;
        
        while(left<=right && right<nums.length){
            currSum += nums[right];
            
            while(right-left+1 == k){
                maxAverage = Math.max(maxAverage, currSum/k);
                currSum -= nums[left];
                left++;
            }
            right++;
        }
        return maxAverage;
        
    }
}